#!/usr/local/bin/python3.6
"""
This program uses the Faker module to generate data for
populating the database tables for C195 - Software II.
"""

from database import *
import datetime
from faker import Faker
from peewee import fn
import random
import settings


def main(settings):
    seed_countries()

    generator = Faker()
    seed_cities(generator, settings.NUM_CITIES)
    seed_addresses(generator, settings.NUM_ADDRESSES)
    seed_customers(generator, settings.NUM_CUSTOMERS)
    seed_appointments(generator, settings.NUM_APPOINTMENTS)


def seed_countries():
    """ two countries are required """
    Country.create(
        country="United States",
        createdBy="1",
        lastUpdateBy="1"
    )
    Country.create(
        country="Mexico",
        createdBy="1",
        lastUpdateBy="1"
    )


def seed_cities(generator, number_of_cities):
    for _ in range(0, number_of_cities):
        result = Country.select(Country.countryId).order_by(fn.Rand()).limit(1)
        user = random_user()
        City.create(
            city=generator.city(),
            countryId=result[0].countryId,
            createdBy=user,
            lastUpdateBy=user,
        )


def seed_addresses(generator, number_of_addresses):
    for _ in range(0, number_of_addresses):
        #  get an address, split on newlines
        fake_address = generator.address()
        address_list = fake_address.split("\n")
        address1 = address_list[0]
        zipcode = random.randrange(10000, 99999)
        #  if more than 2 items in list, assume list[1] can be address2
        if len(address_list) > 2:
            address2 = address_list[1]
        else:
            address2 = ""

        result = City.select(City.cityId).order_by(fn.Rand()).limit(1)
        city = result[0].cityId
        user = random_user()
        Address.create(
            address=address1,
            address2=address2,
            cityId=city,
            postalCode=zipcode,
            phone=generator.phone_number(),
            createdBy=user,
            lastUpdateBy=user
        )


def seed_customers(generator, number_of_customers):
    for _ in range(0, number_of_customers):
        result = Address.select(Address.addressId).order_by(fn.Rand()).limit(1)
        address = result[0].addressId
        active = random.choice([0, 1])
        user = random_user()
        Customer.create(
            customerName=generator.name(),
            addressId=address,
            active=active,
            createdBy=user,
            lastUpdateBy=user
        )


def seed_appointments(generator, number_of_appointments):
    utc_convert = datetime.timedelta(hours=settings.UTC_OFFSET)
    start = datetime.datetime.now()
    start = start.replace(hour=8, minute=0, second=0, microsecond=0)
    end = start + datetime.timedelta(minutes=15)

    for _ in range(0, number_of_appointments):
        customer = (Customer.select(Customer.customerId, Customer.customerName)
            .order_by(fn.Rand()).limit(1)[0])
        cityName = City.select(City.city).order_by(fn.Rand()).limit(1)[0].city
        user = random_user()

        if start.hour > 16:
            # don't schedule appointments after 5pm, set hours to 8am
            start = start.replace(hour=8)
            start += datetime.timedelta(days=1)
            end = end.replace(hour=8, minute=15)
            end += datetime.timedelta(days=1)

        skip_period = 0
        # if meeting start time on weekend, set start to the following monday
        if start.weekday() == 5:
            skip_period = 2
        elif start.weekday() == 6:
            skip_period = 1

        skip_weekend = datetime.timedelta(days=skip_period)
        start += skip_weekend
        end += skip_weekend

        Appointment.create(
            customerId=customer.customerId,
            title=generator.sentence(),
            description=generator.text(),
            location=cityName,
            contact=customer.customerName,
            url=generator.url(),
            start=start - utc_convert,
            end=end - utc_convert,
            createdBy=user,
            lastUpdateBy=user
        )
        start = start + datetime.timedelta(hours=1)
        end = end + datetime.timedelta(hours=1)


def random_user():
    return User.select(User.userId).order_by(fn.Rand()).limit(1)[0].userId


if __name__ == '__main__':
    print("Started:", datetime.datetime.now())
    main(settings)
    print("Finished:", datetime.datetime.now())
