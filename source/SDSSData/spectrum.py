from astropy.io import fits
from astropy.convolution import convolve, Gaussian1DKernel
import numpy
import os


def find_lyman_break(SpectralDataObject):
    #smooth the data first because its noisy
    gauss_kernel = Gaussian1DKernel(5)
    smoothed_data = convolve(SpectralDataObject, gauss_kernel)


class SpectralData(object):

    def __init__(self, filepath=None):
        if filepath == None:
            raise FilePathNotSpecified("File has not been specified")
        self.filepath = filepath

        return

    @property
    def ra(self):
<<<<<<< HEAD
        if getattr(self,'right_ascension',None) is None:
            file = fits.open(self.filepath)

            self.right_ascension = float(file[0].header["RA"])
=======
        if self.right_ascension == None:
            with fits.open(self.filepath) as file
                self.right_ascension = float(file[0].header["RA"])
>>>>>>> 038ff2cf9081cb18e3ed11a2f899b10b5b04c923
            
        return self.right_ascension

    @property
    def dec(self):
<<<<<<< HEAD
        if getattr(self,'declination',None) is None:
            file = fits.open(self.filepath)
            self.declination = float(file[0].header["DEC"])
=======
        if self.declination == None:
            with fits.open(self.filepath) as file
                self.declination = float(file[0].header["DEC"])
>>>>>>> 038ff2cf9081cb18e3ed11a2f899b10b5b04c923

        return self.declination

    @property
    def standard_deviation(self):
        if getattr(self,'rms',None) is None:
            file = fits.open(self.filepath)
            flux_column = file[1].data['flux']
            self.rms = numpy.std(flux_column)
        return self.rms


class FilePathNotSpecified(Exception):
    pass
