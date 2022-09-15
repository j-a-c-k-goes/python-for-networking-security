""" command-line arguments provided to a script are exposed via sys.argv, import the sys module """

import sys
import argparse

parser = argparse.ArgumentParser(description="testing parameters")
parser.add_argument("--party", dest="param1", help="parameter1")
parser.add_argument("--sleep", dest="param2", help="parameter2")
parser.add_argument("--read", dest="param3", type=bool, help="parameter 3 true/false")

params = parser.parse_args()

print("parameter 1", params.param1)
print("parameter 2", params.param2)
print("parameter 3", params.param3)
