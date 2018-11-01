from SDSSData.spectrum import SpectralData 
from astropy.io import fits

filelist = list()

# Takes keyword (ex. 'ra,dec,etc.') and the min/max
# for that keyword. Returns list of all filenames
# within the range.
def search(filenames,keyword,min_ang,max_ang):
    for filename in filenames:
        data = SpectralData(filename)
        if min_ang < data.keyword < max_ang:
            filelist.append(filename)
    return filelist
