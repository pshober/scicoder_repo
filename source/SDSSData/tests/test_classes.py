import numpy as np
from ..spectrum import SpectralData

# Remember to change to relative file paths ---v
files = ['/home/dfn-user/Documents/Repositories/Paddys-SDSS-Repo/scicoder_repo/data/spec-4055-55359-0001.fits',
         '/home/dfn-user/Documents/Repositories/Paddys-SDSS-Repo/scicoder_repo/data/spec-4055-55359-0006.fits',
         '/home/dfn-user/Documents/Repositories/Paddys-SDSS-Repo/scicoder_repo/data/spec-4055-55359-0010.fits',
         '/home/dfn-user/Documents/Repositories/Paddys-SDSS-Repo/scicoder_repo/data/spec-4055-55359-0012.fits']

def test_class_ra():
    '''test the SpectralData class is returning the proper ra'''
    spectral_data = SpectralData(files[0])
    ra = spectral_data.ra
    assert 0 < ra < 360 # the ra is a float between 0 and 2pi
    
def test_class_dec():
    '''test the SpectralData class is returning the proper dec'''
    spectral_data = SpectralData(files[0])
    dec = spectral_data.dec
    assert -180 < dec < 180 # the dec is a float between -pi/2 and pi/2
