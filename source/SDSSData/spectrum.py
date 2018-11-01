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
        self.right_ascension = None
        self.declination = None
        self.rms = None

        return

    @property
    def ra(self):
        if self.right_ascension == None:
            with fits.open(self.filepath) as file
                self.right_ascension = float(file[0].header["RA"])
            
        return self.right_ascension

    @property
    def dec(self):
        if self.declination == None:
            with fits.open(self.filepath) as file
                self.declination = float(file[0].header["DEC"])

        return self.declination

    @property
    def standard_deviation(self):
        if self.rms == None:
            file = fits.open(self.filepath)
            flux_column = file[1].data['flux']
            self.rms = numpy.std(flux_column)
        return self.rms


class FilePathNotSpecified(Exception):
    pass
