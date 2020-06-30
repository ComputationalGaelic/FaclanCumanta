# faclan_cumanta.pròiseact.feumalasan

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
    return os.path.join(pasgan_pròiseict(), 'faclair')

def faigh_faidhlichen_faclair():
    return glob.glob(os.path.join(pasgan_faclair(), '*.json'))