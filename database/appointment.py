import datetime
from .mysqlmodel import MySQLModel
from peewee import *


class Appointment(MySQLModel):
    class Meta:
        db_table = 'appointment'

    appointmentId = IntegerField(primary_key=True)
    customerId = IntegerField(null=False)
    title = CharField(null=False)
    description = TextField(null=False)
    location = TextField(null=False)
    contact = TextField(null=False)
    url = CharField(null=False)
    start = DateTimeField(null=False)
    end = DateTimeField(null=False)
    createDate = DateTimeField(default=datetime.datetime.now)
    createdBy = CharField(null=False)
    lastUpdateBy = CharField(null=False)
