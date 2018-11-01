from SDSSData import search, spectrum
from astropy.io import fits
import argparse
import sys

parser = argparse.ArgumentParser(description="reads fit file and returns ra, dec")

parser.add_argument("-f", "--files", help="the list of fits files to process", nargs="+")
parser.add_argument("-min", "--min", help="minimum of search range", default=0)
parser.add_argument("-max", "--max", help="maximum of search range", default=0)
parser.add_argument("-k", "--keyword",help="keyword to search", default="ra")
args = parser.parse_args()

if args.min > args.max:
	print("minimum range value is larger than max, check your range values.")
	sys.exit(1)

data_list = args.files

passed_files = search(data_list, args.keyword, args.min, args.max)

print(passed_files) 

# for spectrum in spectra:
#     ra = spectrum.ra
#     dec = spectrum.dec
#     sigma = spectrum.standard_deviation
