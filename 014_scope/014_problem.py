class Difference:
    def __init__(self, arr):
        self.maximum_difference = None
        self.__elements = arr

    # Add your code here
    def compute_difference(self):
        self.maximum_difference = max(self.__elements) - min(self.__elements)


# End of Difference class

_ = input()
elements_array = [int(e) for e in input().split(' ')]
# elements_array = [4, 1, 2]

d = Difference(elements_array)
d.compute_difference()

print(d.maximum_difference)
