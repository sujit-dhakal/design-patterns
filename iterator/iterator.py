# numbers = [1,2,3,4,5]
# my_interator = iter(numbers)

# while True:
#     try:
#         print(next(my_interator))
#     except StopIteration:
#         print("iteration finished")
#         break

# Above is built in iterator

# Iterator pattern is used to create and iterator manually

from abc import ABC,abstractmethod

class Iterator(ABC):

    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __next__(self):
        pass

class NumberIterator(Iterator):
    def __init__(self,collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self

class IterableCollection(ABC):
    @abstractmethod
    def __iter__(self):
        pass

class NumberCollection(IterableCollection):
    def __init__(self):
        self._items = []
    def add_item(self,item):
        self._items.append(item)
    def __iter__(self):
        return NumberIterator(self._items)

if __name__ == '__main__':
    collection = NumberCollection()
    collection.add_item(1)
    collection.add_item(2)
    iterator = iter(collection)
    for num in iterator:
        print(num)