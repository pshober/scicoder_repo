from SDSSData.spectrum import SpectralData 
from astropy.io import fits

# Takes keyword (ex. 'ra,dec,etc.') and the min/max
# for that keyword. Returns list of all filenames
# within the range.
def search(filenames,keyword,min_ang,max_ang):
    filelist = list()
    for filename in filenames:
        data = SpectralData(filename)
        if keyword == 'right_ascension':
            try: 
                if min_ang < data.right_ascension < max_ang:
                    filelist.append(filename)
            except TypeError: 
                pass 
        elif keyword == 'declination': 
            try: 
                if min_ang < data.declination < max_ang: 
                    filelist.append(filename)
            except TypeError: 
                pass 
    return filelist
