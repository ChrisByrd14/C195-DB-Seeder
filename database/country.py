"""
"""

import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class Country(MySQLModel):
    class Meta:
        db_table = 'country'

    countryId = IntegerField(primary_key=True)
    country = CharField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createdBy = CharField(null=False)
    lastUpdateBy = CharField(null=False)
