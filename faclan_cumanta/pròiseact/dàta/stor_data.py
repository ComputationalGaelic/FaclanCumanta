# faclan_cumanta.stòr_dàta

# python
import json

# peewee
from peewee import fn

# faclan_cumanta
from .feumalasan import faigh_faidhlichen_faclair
from .modailean import (
    Facal,
    Fuaim,
    tòisich,
    làimhsiche_modail
)

def lòdaich():
    tòisich()
    for ràs in faigh_faidhlichen_faclair():
        dàta = json.load(open(ràs))
        dèanadair = làimhsiche_modail().get(dàta['type'])
        seata = dàta['set_name']
        for baid, faclan in enumerate(dàta['word_sets']):
            for facal in faclan:
                dèanadair(facal, seata, baid)

# faclan
def faclan_le_fuaim_aig_an_toisich(fuaim, co_mheud=None):
    return Facal.select().where(
        Facal.litrichean.startswith(fuaim)
    )

def faclan_le_fuaim_aig_an_deireadh(fuaim, co_mheud=None):
    return Facal.select().where(
        Facal.litrichean.endswith(fuaim)
    )

def faclan_le_fuaim_aig_am_meadhan(fuaim, co_mheud=None):
    return Facal.select().where(
        Facal.litrichean.contains(fuaim) &
        ~(Facal.litrichean.startswith(fuaim)) & 
        ~(Facal.litrichean.endswith(fuaim))
    )
    #Facal.litrichean.iregexp(fuaim)

# fuaimean
def fuaim_tuaireamach():
    return Fuaim.select().order_by(fn.Random()).first()
