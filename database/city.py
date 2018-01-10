import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class City(MySQLModel):
    class Meta:
        db_table = 'city'

    cityId = IntegerField(primary_key=True)
    city = CharField(null=False)
    countryId = IntegerField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createdBy = CharField(null=False)
    lastUpdateBy = CharField(null=False)
