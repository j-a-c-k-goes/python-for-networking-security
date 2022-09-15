""" python is an object oriented language; classes can be created and instantiated """

# create the class
class protocol(object):
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
           
    def getProtocolInfo(self):
        return [self.name,str(self.number),self.description]

# build an object by instantiating the class
protocol_http = protocol("HTTP", 80, "hypertext transfer protocol")

# access the objects attributes and methods
protocol_http.name
protocol_http.number
protocol_http.description
print(protocol_http.getProtocolInfo())