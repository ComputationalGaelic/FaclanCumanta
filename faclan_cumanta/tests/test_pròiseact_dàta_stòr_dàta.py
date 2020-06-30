# tests.test_pròiseact_dàta_stòr_dàta

# python
import types

# peewee
import peewee

# faclan_cumanta
from faclan_cumanta.pròiseact.dàta import stòr_dàta

# tests
from . import settings

def test_lòdaich():
    stòr_dàta.lòdaich(ainm_stòir_dhàta=settings.TEST_DB)

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