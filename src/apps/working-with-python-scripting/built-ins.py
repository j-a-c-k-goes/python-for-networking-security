""" view all of python's built in functions """

import builtins
numberof = len(dir(builtins))
print("how many built-in functions are there?", numberof)
listof = list(dir(builtins))
for function in listof:
    print("built-in function:", function)

