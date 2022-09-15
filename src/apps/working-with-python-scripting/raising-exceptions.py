# triggering a zero division error
def division(a,b):
    return a/b
def calculate():
    division(1,0)
#print(calculate())

# raising an exception
try:
    print("10/0 =", str(10/0))
except Exception as exception:
    print("error =", str(exception))

# IOError, file not found 
try:
    f = open("file.txt", "r")
except Exception as exception:
    print("file not found:", str(exception))
    
    