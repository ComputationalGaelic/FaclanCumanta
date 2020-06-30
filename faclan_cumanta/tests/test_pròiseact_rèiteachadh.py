# tests.test_pròiseact_rèiteachadh

# papersizes
from papersizes import PaperSize

# faclan_cumanta
from faclan_cumanta.pròiseact import rèiteachadh

def test_cruth_clò():
    assert rèiteachadh.CRUTH_CLÒ
    assert type(rèiteachadh.CRUTH_CLÒ) is str

def test_meud_cruth_clò():
    assert rèiteachadh.MEUD_CRUTH_CLÒ
    assert type(rèiteachadh.MEUD_CRUTH_CLÒ) is int

def test_meud_duilleige():
    assert rèiteachadh.MEUD_DUILLEIGE
    assert type(rèiteachadh.MEUD_DUILLEIGE) is PaperSize

def test_meud_loidhne():
    assert rèiteachadh.MEUD_LOIDHNE
    assert type(rèiteachadh.MEUD_LOIDHNE) is int

def test_marghan():
    assert rèiteachadh.MARGHAN
    assert type(rèiteachadh.MARGHAN) is int

def test_ainm_stòir_dhàta():
    assert rèiteachadh.AINM_STÒIR_DHÀTA
    assert type(rèiteachadh.AINM_STÒIR_DHÀTA) is str