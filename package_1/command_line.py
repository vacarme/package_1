import argparse
from package_1.module_1 import haversine
from termcolor import colored


def main():
    description = 'stkrgcp_description'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--coords',
                        nargs='+',
                        help='list of coordinates',
                        required=False)
    parser.add_argument('--prod',
                        action='store_true',
                        default=False,
                        help='Example here')
    args = parser.parse_args()
    lon1, lat1, lon2, lat2 = args.coords
    dist = haversine(float(lon1), float(lat1), float(lon2), float(lat2))
    print(colored("###### Distance ######", "yellow"))
    print(colored(dist, "red"))
