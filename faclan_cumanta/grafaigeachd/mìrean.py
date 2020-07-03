# faclan_cumanta.grafaigeachd.mìrean

from .aonadan import òirlich_gu_pongan

class CliathFaclan:
    def __init__(self, faclan, reandaraiche):
        self.reandaraiche = reandaraiche
        self.faclan = [
            CliathLitir(
                f.litrichean, 
                self.reandaraiche.co_theacsa
            ) for f in faclan
        ]

    def dèan(self, x, y, beàrnadh):
        for facal in self.faclan:
            facal.dèan(x, y)
            y += facal.àirde + beàrnadh

class CliathLitir:
    def __init__(self, litrichean, co_theacsa):
        self.litrichean = litrichean
        self.co_theacsa = co_theacsa
        self.leud = òirlich_gu_pongan(1)
        self.àirde = òirlich_gu_pongan(1)
        self.cùrsa_x = 1
        self.cùrsa_y = 0

    def dèan(self, x, y):
        self.co_theacsa.save()
        self.co_theacsa.translate(x, y)
        for inneacs, litir in enumerate(self.litrichean):
            self.dèan_litir(inneacs, litir)
        self.co_theacsa.restore()

    def dèan_litir(self, inneacs, litir):
        self.co_theacsa.save()
        self.co_theacsa.translate(
            self.leud * (inneacs * self.cùrsa_x), 
            self.àirde * (inneacs * self.cùrsa_y)
        )
        (x, y, leud, àirde, dx, dy) = self.co_theacsa.text_extents(litir)
        self.co_theacsa.save()
        self.co_theacsa.translate(self.leud/2 - leud/2, self.àirde-2) 
        self.co_theacsa.show_text(litir)
        self.co_theacsa.restore()
        self.co_theacsa.rectangle(0, 0, self.leud, self.àirde)
        self.co_theacsa.stroke()
        self.co_theacsa.restore()

