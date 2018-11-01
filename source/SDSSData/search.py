from SDSSData.spectrum import SpectralData 
from astropy.io import fits

filelist = list()

# Takes keyword (ex. 'ra,dec,etc.') and the min/max
# for that keyword. Returns list of all filenames
# within the range.
def search(filenames,keyword,min_ang,max_ang):
    for filename in filenames:
        data = SpectralData(filename)
        if keyword == 'ra': 
            if min_ang < data.ra < max_ang:
                filelist.append(filename)
        elif keyword == 'dec': 
            if min_ang < data.dec < max_ang: 
                filelist.append(filename) 
    return filelist
