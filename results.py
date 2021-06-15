from wrapper import REQUEST_MAP
import sys

firstarg = sys.argv[1]

def search_map(filename):
    while True:
        try:
            if REQUEST_MAP[filename]:
                return REQUEST_MAP[filename]
        except KeyError:
            continue

search_map(firstarg)
