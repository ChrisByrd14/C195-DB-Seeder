from .address import Address
import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class Customer(MySQLModel):
    class Meta:
        db_table = 'customer'

    customerId = IntegerField(primary_key=True)
    customerName = CharField(null=False)
    addressId = IntegerField(null=False)
    active = IntegerField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createdBy = CharField(null=False)
    lastUpdateBy = CharField(null=False)
