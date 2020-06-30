# tests.test_pròiseact_dàta_modailean

# python
import types

# peewee
from peewee import SqliteDatabase

# faclan_cumanta
from faclan_cumanta.pròiseact.dàta import modailean

# tests
from . import settings

def test_db():
    assert modailean.db
    assert type(modailean.db) is SqliteDatabase

def test_dèan_facal():
    modailean.tòisich(ainm_stòir_dhàta=settings.TEST_DB)
    result = modailean.dèan_facal('test_facal', 'test_seata', 100)
    assert result
    assert isinstance(result, modailean.Facal)
    assert result.litrichean == 'test_facal'
    assert result.seata == 'test_seata'
    assert result.baid == 100

def test_dèan_fuaim():
    modailean.tòisich(ainm_stòir_dhàta=settings.TEST_DB)
    result = modailean.dèan_fuaim('test_fuaim', 'test_seata', 100)
    assert result
    assert isinstance(result, modailean.Fuaim)
    assert result.litrichean == 'test_fuaim'
    assert result.seata == 'test_seata'
    assert result.baid == 100

def test_tòisich():
    modailean.tòisich(ainm_stòir_dhàta=settings.TEST_DB)
    tables = modailean.db.get_tables()
    assert 'facal' in tables
    assert 'fuaim' in tables

def test_làimhsiche_modail():
    assert modailean.làimhsiche_modail()
    assert type(modailean.làimhsiche_modail()) is dict
    assert 'faclan' in modailean.làimhsiche_modail()
    assert type(modailean.làimhsiche_modail()['faclan']) is types.FunctionType
    assert 'fuaimean' in modailean.làimhsiche_modail()
    assert type(modailean.làimhsiche_modail()['fuaimean']) is types.FunctionType