import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class User(MySQLModel):
    class Meta:
        db_table = 'user'

    userId = IntegerField(primary_key=True)
    userName = CharField(null=False)
    password = IntegerField(null=False)
    active = IntegerField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createBy = CharField(null=False)
    lastUpdatedBy = CharField(null=False)
