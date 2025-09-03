# class RandomizedSet:

#     def __init__(self):
#         self.value = set([])

#     def insert(self, val: int) -> bool:
#         if val in self.value:
#             return False
#         self.value.add(val)
#         return True

#     def remove(self, val: int) -> bool:
#         if val in self.value:
#             self.value.remove(val)
#             return True
#         return False

#     def getRandom(self) -> int:
#         return random.choice(list(self.value))


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()

import random


class RandomizedSet:

    def __init__(self):
        self.mapList = []
        self.mapValues = {}

    def insert(self, val: int) -> bool:
        if val in self.mapValues:
            return False

        self.mapValues[val] = len(self.mapList)
        self.mapList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapValues:
            return False

        lastElement = self.mapList[-1]
        indexToBeRemoved = self.mapValues[val]

        self.mapList[indexToBeRemoved] = lastElement
        self.mapValues[lastElement] = indexToBeRemoved

        self.mapList.pop()
        del self.mapValues[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.mapList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
