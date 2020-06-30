# faclan_cumanta.pròiseact.dàta.stòr_dàta

# python
import json

# peewee
from peewee import fn

# faclan_cumanta
from ..feumalasan import faigh_faidhlichen_faclair
from .modailean import (
    Facal,
    Fuaim,
    tòisich,
    làimhsiche_modail
)

def lòdaich(ainm_stòir_dhàta=None):
    tòisich(ainm_stòir_dhàta = ainm_stòir_dhàta)
    Facal.delete().execute()
    Fuaim.delete().execute()
    for ràs in faigh_faidhlichen_faclair():
        dàta = json.load(open(ràs))
        dèanadair = làimhsiche_modail().get(dàta['type'])
        seata = dàta['set_name']
        for baid, faclan in enumerate(dàta['word_sets']):
            for facal in faclan:
                dèanadair(facal, seata, baid)

# faclan
foincseanan_seòrsa = {
    'litir': Facal.litrichean,
    'seata': Facal.seata,
    'baid': Facal.baid,
    'air thuairmeas': fn.Random(),
}

def criathraich_faclan(
        faclan, 
        seata=None, 
        baid=None, 
        seòrsaich_le=None, 
        co_mheud=None
    ):
    if seata:
        faclan = faclan.where(Facal.seata == seata)
    if baid:
        faclan = faclan.where(Facal.baid == baid)
    if foincseanan_seòrsa.get(seòrsaich_le):
        faclan = faclan.order_by(foincseanan_seòrsa.get(seòrsaich_le))
    if co_mheud:
        faclan = faclan.limit(co_mheud)
    return faclan

def faclan_le_fuaim_aig_an_toisich(
        fuaim, 
        seata=None, 
        baid=None, 
        seòrsaich_le=None, 
        co_mheud=None
    ):
    return criathraich_faclan(
        Facal.select().where(
            Facal.litrichean.startswith(fuaim)
        ), 
        seata=seata, 
        baid=baid, 
        seòrsaich_le=seòrsaich_le,
        co_mheud=co_mheud
    )
    
def faclan_le_fuaim_aig_an_deireadh(
        fuaim, 
        seata=None, 
        baid=None, 
        seòrsaich_le=None, 
        co_mheud=None
    ):
    return criathraich_faclan(
        Facal.select().where(
            Facal.litrichean.endswith(fuaim)
        ), 
        seata=seata, 
        baid=baid, 
        seòrsaich_le=seòrsaich_le,
        co_mheud=co_mheud
    )

def faclan_le_fuaim_aig_am_meadhan(
        fuaim, 
        seata=None, 
        baid=None, 
        seòrsaich_le=None, 
        co_mheud=None
    ):
    return criathraich_faclan(
        Facal.select().where(
            Facal.litrichean.contains(fuaim) &
            ~(Facal.litrichean.startswith(fuaim)) & 
            ~(Facal.litrichean.endswith(fuaim))
        ), 
        seata=seata, 
        baid=baid, 
        seòrsaich_le=seòrsaich_le,
        co_mheud=co_mheud
    )

def faclan_le_eas_preisean_riaghailteach(
        pàtran, 
        seata=None, 
        baid=None, 
        seòrsaich_le=None, 
        co_mheud=None
    ):
    return criathraich_faclan(
        Facal.select().where(
            Facal.litrichean.regexp(pàtran)
        ), 
        seata=seata, 
        baid=baid, 
        seòrsaich_le=seòrsaich_le,
        co_mheud=co_mheud
    )

# fuaimean
def fuaim_tuaireamach():
    return Fuaim.select().order_by(fn.Random()).first()
