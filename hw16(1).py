# import re


# class SimpleIterator():
#     def __init__(self,limit):
#         self.limit = limit
#         self.counter= 0 

#     def __next__(self):
#         if self.limit>self.counter:
#             self.counter +=1
#             return self.counter
#         else:
#             raise StopIteration


# iterator =SimpleIterator(5)
# print(next(iterator)) 





# def my_generator(val):
#     while val >0:
#         val-=1
#         yield val


# gen= my_generator(10)
# print(next(gen))


nums= list(x**2 for x in range(1000))
print(nums)