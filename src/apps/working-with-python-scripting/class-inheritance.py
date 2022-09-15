""" inheritance allows creation of a new class from another """

class MyList(list):
    def max_min(self):
        return max(self), min(self)
myList = MyList()
myList.extend([100,200,300,500])
print(myList)
print(myList.max_min())