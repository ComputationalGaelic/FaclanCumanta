# faclan_cumanta.grafaigeachd.reandaraichean

# python
import json

# cairo
import cairo

# papersizes
from papersizes.parse import paper_size

# faclan_cumanta
from faclan_cumanta.pròiseact import (
    feumalasan,
    rèiteachadh
)

# http://www.tortall.net/mu/wiki/CairoTutorial

"""
need a layout object that will draw baselines
and position text correctly on page
also add in template features, i.e. ainm, deit, ceann-sgrìobhadh, etc.
"""

class ReandaraicheDeuchainne:
    cruth_clò = rèiteachadh.CRUTH_CLÒ
    meud_cruth_clò = rèiteachadh.MEUD_CRUTH_CLÒ
    meud_duilleige = rèiteachadh.MEUD_DUILLEIGE
    meud_loidhne = rèiteachadh.MEUD_LOIDHNE
    marghan = rèiteachadh.MARGHAN

    def __init__(self, slighe_faidhle):
        self.slighe_faidhle = slighe_faidhle
        self.uachdar = cairo.PDFSurface(
            self.slighe_faidhle, 
            self.meud_duilleige.width, 
            self.meud_duilleige.height
        )
        self.co_theacsa = cairo.Context(self.uachdar)

    def sgrìobh(self):
        self.uachdar.show_page()

    def dèan_loidhneachan(self):
        self.co_theacsa.set_source_rgb(0.46, 0.66, 0.87)
        self.co_theacsa.set_line_width(1)
        self.co_theacsa.move_to(self.marghan, self.marghan)
        for l in range(6):
            self.co_theacsa.move_to(
                self.marghan, 
                self.marghan + (l * self.meud_loidhne)
            )
            self.co_theacsa.line_to(
                self.meud_duilleige.width - self.marghan, 
                self.marghan + (l * self.meud_loidhne)
            )
            self.co_theacsa.stroke()


    def dèan_dealbh(self):
        self.co_theacsa.set_source_rgb(0.1, 0.1, 0.1)
        self.co_theacsa.set_line_width(2)
        self.co_theacsa.select_font_face(
            self.cruth_clò, 
            cairo.FontSlant.NORMAL, 
            cairo.FontWeight.NORMAL
        )
        self.co_theacsa.set_font_size(self.meud_cruth_clò)
        self.co_theacsa.move_to(
            self.marghan, 
            self.marghan
        )
        self.co_theacsa.text_path("Fàilte")
        self.co_theacsa.stroke()

def demo():
    """
    Generates a test page in the current directory.
    """
    r = ReandaraicheDeuchainne('test.pdf')
    r.dèan_loidhneachan()
    r.dèan_dealbh()
    r.sgrìobh()

class Reandaraiche:
    def __init__(self, coltas_duilleige, slighe_faidhle):
        self.slighe_faidhle = slighe_faidhle
        with open(
            feumalasan.faigh_faidhle_coltas_duilleige(coltas_duilleige)
        ) as f:
            self.coltas_duilleige = json.load(f)

    def sgrìobh(self):
        self.uachdar.show_page()

    def tòisich(self):
        self.meud_duilleige = paper_size(
            self.coltas_duilleige['meud agus comhair']
        )
        self.marghan = self.coltas_duilleige['marghan']
        self.beàrnadh = self.coltas_duilleige['beàrnadh']
        self.raointean = self.coltas_duilleige['raointean']
        self.leud_cuirp = self.meud_duilleige.width - self.marghan * 2
        self.uachdar = cairo.PDFSurface(
            self.slighe_faidhle, 
            self.meud_duilleige.width, 
            self.meud_duilleige.height
        )
        self.co_theacsa = cairo.Context(self.uachdar)

    def dèan(self):
        self.dèan_bann_cinn()
        self.dèan_bann_coise()

    def dèan_bann_cinn(self):
        àirde = self.raointean['bann-cinn']
        self.dèan_ceart_cheàrnach(self.marghan, àirde)
        
    def dèan_bann_coise(self):
        àirde = self.raointean['bann-coise']
        y = self.meud_duilleige.height - àirde - self.marghan
        self.dèan_ceart_cheàrnach(y, àirde)

    def dèan_ceart_cheàrnach(self, y, àirde):
        self.co_theacsa.set_source_rgb(0.1, 0.1, 0.1)
        self.co_theacsa.set_line_width(1)
        self.co_theacsa.rectangle(
            self.marghan, 
            y,
            self.leud_cuirp,
            àirde
        )
        self.co_theacsa.stroke()
