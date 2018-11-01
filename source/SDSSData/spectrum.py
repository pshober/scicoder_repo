from astropy.io import fits
import numpy
import os

class SpectralData(object):

    def __init__(self, filepath=None):
        if filepath == None:
            raise FilePathNotSpecified("File has not been specified")
        self.filepath = filepath

        return

    @property
    def ra(self):
        if getattr(self,'right_ascension',None) is None:
            file = fits.open(self.filepath)

            self.right_ascension = float(file[0].header["RA"])
            
        return self.right_ascension

    @property
    def dec(self):
        if getattr(self,'declination',None) is None:
            file = fits.open(self.filepath)
            self.declination = float(file[0].header["DEC"])

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
