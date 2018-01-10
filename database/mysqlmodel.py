"""
"""

from peewee import *
import settings


mysql_db = MySQLDatabase(
    settings.DB_DATABASE,
    host=settings.DB_HOST,
    user=settings.DB_USER,
    password=settings.DB_PASS
)

class MySQLModel(Model):
    class Meta:
        database = mysql_db
