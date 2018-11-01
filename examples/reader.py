from SDSSData.search import search
from SDSSData.spectrum import SpectralData  
from astropy.io import fits
import argparse
import sys
import os 

parser = argparse.ArgumentParser(description="reads fit file and returns ra, dec")

parser.add_argument("-d", "--directory", type=str, help="the directory containing all files to test")
parser.add_argument("-min", "--min", help="minimum of search range", type=float)
parser.add_argument("-max", "--max", help="maximum of search range", type=float)
parser.add_argument("-k", "--keyword",help="keyword to search", choices={'right_ascension','declination'})
args = parser.parse_args()

if args.min > args.max:
	print("minimum range value is larger than max, check your range values.")
	sys.exit(1)

files_list = os.listdir(args.directory) 
data_list  = [os.path.join(args.directory,filename) for filename in files_list]
 
passed_files = search(data_list, args.keyword, args.min, args.max)

print('\n----------------------------------------') 
print('-----Files that satisfy constraints-----') 
print('----------------------------------------\n')
 
print(f"{len(passed_files)} out of {len(files_list)} files satisfy.\n") 

for file in passed_files: 
   print(file) 

# for spectrum in spectra:
#     ra = spectrum.ra
#     dec = spectrum.dec
#     sigma = spectrum.standard_deviation
