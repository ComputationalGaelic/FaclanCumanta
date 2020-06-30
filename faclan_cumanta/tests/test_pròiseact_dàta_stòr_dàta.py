# tests.test_pròiseact_dàta_stòr_dàta

# python
import types

# peewee
import peewee

# faclan_cumanta
from faclan_cumanta.pròiseact.dàta import stòr_dàta
from faclan_cumanta.pròiseact.dàta.modailean import (
    Facal,
    Fuaim,
    db,
    tòisich
)

# tests
from . import settings

def _lòdaich_dàta():
    tòisich(ainm_stòir_dhàta=settings.TEST_DB)
    Facal.delete().execute()
    Fuaim.delete().execute()
    data = [
        (
            settings.TEST_LIOSTA_FACAIL[i],
            settings.TEST_LIOSTA_SEATA[i],
            settings.TEST_LIOSTA_BAID[i]
        ) for i in range(len(settings.TEST_LIOSTA_FACAIL))
    ]
    with db.atomic():
        Facal.insert_many(data, fields=[
            Facal.litrichean,
            Facal.seata,
            Facal.baid 
        ]).execute()

def test_lòdaich():
    stòr_dàta.lòdaich(ainm_stòir_dhàta=settings.TEST_DB)
    assert Facal.select().count() == 223

def test_criathraich_faclan():
    tòisich(ainm_stòir_dhàta=settings.TEST_DB)
    Facal.delete().execute()
    facal = Facal.create(
        litrichean=settings.TEST_FACAL, 
        seata=settings.TEST_SEATA, 
        baid=settings.TEST_BAID
    )
    result = stòr_dàta.criathraich_faclan(
        Facal.select().where(
            Facal.litrichean == settings.TEST_FACAL
        ), 
        seata=settings.TEST_SEATA, 
        baid=settings.TEST_BAID
    )
    assert result.count() == 1
    assert result[0] == facal
    assert result[0].litrichean == settings.TEST_FACAL
    assert result[0].seata == settings.TEST_SEATA
    assert result[0].baid == settings.TEST_BAID

def test_criathraich_faclan_seòrsaich():
    _lòdaich_dàta()
    result = stòr_dàta.criathraich_faclan(
        Facal.select().where(
            Facal.litrichean << settings.TEST_LIOSTA_FACAIL
        ),
        seòrsaich_le='litir'
    )
    assert result.count() == 4
    assert sorted(settings.TEST_LIOSTA_FACAIL) == [f.litrichean for f in result]

def test_criathraich_faclan_co_mheud():
    _lòdaich_dàta()
    result = stòr_dàta.criathraich_faclan(
        Facal.select().where(
            Facal.litrichean << settings.TEST_LIOSTA_FACAIL
        ),
        co_mheud=3
    )
    assert result.count() == 3

def test_foincseanan_seòrsa():
    assert stòr_dàta.foincseanan_seòrsa
    assert type(stòr_dàta.foincseanan_seòrsa) is dict
    assert 'litir' in stòr_dàta.foincseanan_seòrsa
    assert isinstance(
        stòr_dàta.foincseanan_seòrsa['litir'],
        peewee.CharField
    )
    assert stòr_dàta.foincseanan_seòrsa['litir'].name == 'litrichean'
    assert 'seata' in stòr_dàta.foincseanan_seòrsa
    assert isinstance(
        stòr_dàta.foincseanan_seòrsa['seata'],
        peewee.CharField
    )
    assert stòr_dàta.foincseanan_seòrsa['seata'].name == 'seata'
    assert 'baid' in stòr_dàta.foincseanan_seòrsa
    assert isinstance(
        stòr_dàta.foincseanan_seòrsa['baid'],
        peewee.IntegerField
    )
    assert stòr_dàta.foincseanan_seòrsa['baid'].name == 'baid'
    assert 'air thuairmeas' in stòr_dàta.foincseanan_seòrsa
    assert stòr_dàta.foincseanan_seòrsa['air thuairmeas'] == peewee.fn.Random()

def test_faclan_le_fuaim_aig_an_toisich():
    _lòdaich_dàta()
    result = stòr_dàta.faclan_le_fuaim_aig_an_toisich('a')
    assert result.count() == 1
    assert result[0].litrichean == settings.TEST_LIOSTA_FACAIL[0]

def test_faclan_le_fuaim_aig_an_deireadh():
    _lòdaich_dàta()
    result = stòr_dàta.faclan_le_fuaim_aig_an_deireadh('th_')
    assert result.count() == 1
    assert result[0].litrichean == settings.TEST_LIOSTA_FACAIL[1]

def test_faclan_le_fuaim_aig_am_meadhan():
    _lòdaich_dàta()
    result = stòr_dàta.faclan_le_fuaim_aig_am_meadhan('èa')
    assert result.count() == 1
    assert result[0].litrichean == settings.TEST_LIOSTA_FACAIL[3]

