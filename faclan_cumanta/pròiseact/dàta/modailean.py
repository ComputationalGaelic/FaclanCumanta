# faclan_cumanta.modailean

# peewee
from peewee import *

db = SqliteDatabase('db.faclan.sqlite3')

class Facal(Model):
    litrichean = CharField()
    seata = CharField(null=True)
    baid = IntegerField(null=True)

    class Meta:
        database = db

class Fuaim(Model):
    litrichean = CharField()
    seata = CharField(null=True)
    baid = IntegerField(null=True)

    class Meta:
        database = db

def dèan_facal(facal, seata, baid):
    return Facal.create(litrichean=facal, seata=seata, baid=baid)

def dèan_fuaim(facal, seata, baid):
    return Fuaim.create(litrichean=facal, seata=seata, baid=baid)

def tòisich():
    db.connect()
    db.create_tables([Facal, Fuaim])

def làimhsiche_modail():
    return {
        'faclan': dèan_facal,
        'fuaimean': dèan_fuaim,
    }