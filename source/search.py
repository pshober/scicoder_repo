from spectrum import SpectralData
from astropy.io import fits

filelist = list()

# Takes keyword (ex. 'ra,dec,etc.') and the min/max
# for that keyword. Returns list of all filenames
# within the range.
def search(filenames,keyword,min,max):
    for filename in filenames:
        data = SpectralData(filename)
        if min < data.keyword < max:
            filelist.append(filename)
    return filelist
