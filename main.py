#!/usr/local/bin/python3.6
"""
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
        createdBy="admin",
        lastUpdateBy="admin"
    )
    Country.create(
        country="Mexico",
        createdBy="admin",
        lastUpdateBy="admin"
    )


def seed_cities(generator, number_of_cities):
    for _ in range(0, number_of_cities):
        result = Country.select(Country.countryId).order_by(fn.Rand()).limit(1)
        City.create(
            city=generator.city(),
            countryId=result[0].countryId,
            createdBy='admin',
            lastUpdateBy='admin',
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
        Address.create(
            address=address1,
            address2=address2,
            cityId=city,
            postalCode=zipcode,
            phone=generator.phone_number(),
            createdBy='admin',
            lastUpdateBy='admin'
        )


def seed_customers(generator, number_of_customers):
    for _ in range(0, number_of_customers):
        result = Address.select(Address.addressId).order_by(fn.Rand()).limit(1)
        address = result[0].addressId
        active = random.choice([0, 1])
        Customer.create(
            customerName=generator.name(),
            addressId=address,
            active=active,
            createdBy='admin',
            lastUpdateBy='admin'
        )


def seed_appointments(generator, number_of_appointments):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(minutes=15)
    for _ in range(0, number_of_appointments):
        customer = (Customer.select(Customer.customerId, Customer.customerName)
            .order_by(fn.Rand()).limit(1)[0])
        cityName = City.select(City.city).order_by(fn.Rand()).limit(1)[0].city
        Appointment.create(
            customerId=customer.customerId,
            title=generator.sentence(),
            description=generator.text(),
            location=cityName,
            contact=customer.customerName,
            url=generator.url(),
            start=start,
            end=end,
            createdBy='admin',
            lastUpdateBy='admin'
        )
        start = start + datetime.timedelta(hours=1)
        end = end + datetime.timedelta(hours=1)


if __name__ == '__main__':
    print(datetime.datetime.now())
    main(settings)
    print(datetime.datetime.now())
