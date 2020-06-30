# faclan_cumanta.pròiseact.dàta.modailean

# peewee
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField
)

# faclan_cumanta
from faclan_cumanta.pròiseact import rèiteachadh

db = SqliteDatabase(None)

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

def tòisich(ainm_stòir_dhàta=None):
    db.init(ainm_stòir_dhàta or rèiteachadh.AINM_STÒIR_DHÀTA)
    db.connect()
    db.create_tables([Facal, Fuaim])

def làimhsiche_modail():
    return {
        'faclan': dèan_facal,
        'fuaimean': dèan_fuaim,
    }