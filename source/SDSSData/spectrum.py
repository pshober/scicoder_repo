from astropy.io import fits

import os

def SpectrumSearch(path, z, kind, mag):

    return



class SpectralData(object):

    def __init__(self, filepath=None):
        if filepath == None:
            raise FilePathNotSpecified("File has not been specified")
        self.filepath = filepath
        self.data = sfits.open(filepath)
        self.right_ascension = None
        self.declination = None

        return

    @property
    def ra(self):
        if self.right_ascension == None:
            self.right_ascension = self.data.header["RA"]

        return self.right_ascension

    @property
    def dec(self):
        if self.declination == None:
            self.declination = self.data.header["DEC"]

        return self.declination


class FilePathNotSpecified(Exception):
    pass
