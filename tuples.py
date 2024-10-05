#immutable ordered , cannot be changed after creation
mutuple=("max",)
print(mutuple)

mutuple1=tuple(["max",90,"bad"])
item=mutuple1[1]
print(item)

for i in mutuple1:
    print(i)

if 90 in mutuple1:
    print("yes")

print(mutuple.count("max"))

print(mutuple1.index(90))

#convert tuple to list and vice versa
mylist=list(mutuple)
print(mylist)

mutuple=tuple(mylist)
print(mutuple)

#SLICING
a = (1,2,3,4,5,6)
b = a[:4]
c=  a[::-1]
print(f"{a}\t{b}")

#unpacking
name,age,surname=mutuple1
print(f"{name}\t{age}\t{surname}")

#compare tuple and list --large data ->tuple more efficient
#data size comaparing
import sys
list1 = [0,1,2, "hello", True]
tuple1= (0,1,2, "hello", True)
print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple1), "bytes")

#timecomparision
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000))

