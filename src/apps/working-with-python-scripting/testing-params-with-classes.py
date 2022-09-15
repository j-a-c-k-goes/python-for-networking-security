""" classes lead to more readable code, used here as global object for params """

import argparse
class Parameters:
    """global parameters"""
    def __init__(self, **kwargs):
        self.param1 = kwargs.get("param1")
        self.param2 = kwargs.get("param2")
    def viewParameters(inputParameters):
        print(inputParameters.param1)
        print(inputParameters.param2)

parser = argparse.ArgumentParser(description="passing parameters into an object")
parser.add_argument("-p1", dest="param1", help="parameter1")
parser.add_argument("-p2", dest="param2", help="parameter2")
params = parser.parse_args()

inputParameters = Parameters(param1=params.param1, param2=params.param2)
inputParameters.viewParameters()
        