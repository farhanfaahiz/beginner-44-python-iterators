a = [1, 2, 3, 5, 6, 4]
print(a)

it = iter(a)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

#using class for iterator

class ListIterator:
    def __init__(self, list):
        self.__list = list
        self.__index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration("that's not part of it")
        return self.__list[self.__index]
    
mylist = ListIterator(a)
it = iter(mylist)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#for i in it:
#    print(i)