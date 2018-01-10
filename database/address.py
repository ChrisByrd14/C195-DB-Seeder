import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class Address(MySQLModel):
    class Meta:
        db_table = 'address'

    addressId = IntegerField(primary_key=True)
    address = CharField(null=False)
    address2 = CharField(null=False)
    cityId = IntegerField(null=False)
    postalCode = CharField(null=False)
    phone = CharField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createdBy = CharField(null=False)
    lastUpdateBy = CharField(null=False)
