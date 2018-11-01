import numpy as np
from .SDSSData.spectrum import SpectralData

files = ['../../data/spec-4055-55359-0001.fits',
         '../../data/spec-4055-55359-0006.fits',
         '../../data/spec-4055-55359-0010.fits',
         '../../data/spec-4055-55359-0012.fits']

def test_class_ra():
    'test the SpectralData class is returning the proper ra'
    spectral_data = SpectralData(files[0])
    ra = spectral_data.ra
    assert 0 < ra < 2*np.pi # the ra is a float between 0 and 2pi
    
def test_class_dec():
    'test the SpectralData class is returning the proper dec'
    spectral_data = SpectralData(files[0])
    dec = spectral_data.dec
    assert -np.pi < dec < np.pi # the dec is a float between -pi/2 and pi/2
