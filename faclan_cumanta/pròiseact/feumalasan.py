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

def pasgan_coltasan_duilleige():
    return os.path.join(pasgan_pròiseict(), 'coltasan_duilleige')

def faigh_faidhlichen_faclair():
    return glob.glob(os.path.join(pasgan_faclair(), '*.json'))

def faigh_faidhle_coltas_duilleige(ainm):
    return os.path.join(pasgan_coltasan_duilleige(), '{0}.json'.format(ainm))