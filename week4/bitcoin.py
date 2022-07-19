import sys
import requests

r = requests.request()

try:
	bitcoins = float(sys.argv[1])
except ValueError:
	sys.exit("Value isn't a float")
except IndexError:
	sys.exit("No value specified.")

print(bitcoins)

# TODO the rest
# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
