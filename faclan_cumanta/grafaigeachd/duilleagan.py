# faclan_cumanta.grafaigeachd.duilleagan

"""
stoidhle duilleige: page style

duilleag-stoidhle: stylesheet

comhair na duilleige: orientation

cùl-raon: background
"""

# faclan_cumanta
from faclan_cumanta.pròiseact import rèiteachadh

class ColtasDuilleige():
    cruth_clò = rèiteachadh.CRUTH_CLÒ
    meud_cruth_clò = rèiteachadh.MEUD_CRUTH_CLÒ
    meud_duilleige = rèiteachadh.MEUD_DUILLEIGE
    meud_loidhne = rèiteachadh.MEUD_LOIDHNE
    marghan = rèiteachadh.MARGHAN

class Duilleag():
    def __init__(self):
        self.raointean = {}

    def cuir_raon_ris(self, raon):
        self.raointean[raon.ainm] = raon


class RaonDuilleige():
    def __init__(self, ainm, stuth=None):
        self.ainm = ainm
        self.stuth = stuth

    def reandaraich(self, )