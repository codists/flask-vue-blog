# # Base class definition
# class ClassA(object):
#     def __init__(self):
#         print("Initializing A")
#
#     # hoping that this function is called by this class's printFnX
#     def fnX(self, x):
#         return x ** 2
#
#     def printFnX(self, x):
#         print("ClassA:", self.fnX(x))
#
#
# # Inherits from ClassA above
# class ClassB(ClassA):
#     def __init__(self):
#         print("initizlizing B")
#
#     def fnX(self, x):
#         return 2 * x
#
#     def printFnX(self, x):
#         print("ClassB:", self.fnX(x))
#         ClassA.printFnX(self, x)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)


class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
