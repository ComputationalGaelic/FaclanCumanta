# faclan_cumanta.feumalasan

# python
import inspect
import glob
import os

def pasgan_pròiseict():
    return os.path.dirname(
        os.path.abspath(
            inspect.getfile(inspect.currentframe())
        )
    )

def pasgan_faclair():
    return '{0}/faclair'.format(pasgan_pròiseict())

def faigh_faidhlichen_faclair():
    return glob.glob('{0}/*.json'.format(pasgan_faclair()))