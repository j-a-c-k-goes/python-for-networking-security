""" get information about methods from a specific moduel using dir() method """

import math
for name in dir(math):
    print(name, end="\t")

