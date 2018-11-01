from astropy.io import fits
import os

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
            file = fits.open(self.filepath)

            self.right_ascension = float(file[0].header["RA"])
            
        return self.right_ascension

    @property
    def dec(self):
        if self.declination == None:
            file = fits.open(self.filepath)
            self.declination = float(file[0].header["DEC"])

        return self.declination

    @property
    def standard_deviation(self):
        file = fits.open(self.filepath)


class FilePathNotSpecified(Exception):
    pass
