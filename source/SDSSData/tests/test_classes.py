
from .SDSSData.spectrum import SpectralData

files = ['../../../data/spec-4055-55359-0001.fits',
         '../../../data/spec-4055-55359-0006.fits',
         '../../../data/spec-4055-55359-0010.fits',
         '../../../data/spec-4055-55359-0012.fits']

def test_class_ra():
    'test the SpectralData class is returning the proper ra'
    assert # the ra is a float between 0 and 2pi
    
def test_class_dec():
    'test the SpectralData class is returning the proper dec'
    assert # the dec is a float between -pi/2 and pi/2
