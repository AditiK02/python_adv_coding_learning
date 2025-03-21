my_list=["apple",24,"apple",'sdg']
print(my_list)

list1=list()
print(list1)

my_list2=list("a psp9")
print(my_list2)
my_list2=my_list2[::-1]

y=''.join(my_list2)
print(y, "this is y")
print(y, "this is y")

kk=[]
sentence="This is my cat"
print(sentence)
lin=sentence.split(" ")
kk=lin.reverse()
print(' '.join(lin))


if 24 and "apple" or "cho"in my_list:
    print("yes")
else:
    print("no")

#METHODS IN LIST

print(len(list1))

my_list2.append(24)
print(my_list2)

my_list2.insert(1,"blueberry")
print(my_list2)

last_item=my_list2.pop()
print(last_item)
print(my_list2)


item1=my_list2.remove("a")
print(item1)
print(my_list2)

itm2=my_list.reverse() # changes the original list
print(my_list)

int_list=[-1,-2,7,5,-9]
itm3=int_list.sort()  # sort === it changes the original list
print(int_list)

int_list2=[0,-9,7,-3]
new_int_list=sorted(int_list2) #sorted === mekes changes to new list while original list is as it is.
print(int_list2)
print(new_int_list)

list3 = [0] * 5
print(list3)

list3=list3 + int_list
print(list3)

#----------------------------------------
#SLICING
#----------------------------------------
print("-----------slicing---------------") 
sli1=list3[1:8]
print(sli1)

sli2=list3[::2]
print(sli2)

sli3=list3[::-1]
print(sli3)

#----------------------------------------
#COPYING
#----------------------------------------

orig_list=["banana","apple","orange"]

copy_lis=orig_list # wrong copying method

copy_lis.append("lemon")

print(copy_lis)
print(orig_list)  #original list is also altered so this method of assignment will not work

#use copy() method
copy_lis=orig_list.copy()
#use list function
copy_lis=list(orig_list)
#use slicing [:] ene to end
copy_lis=orig_list[:]
# use for loop
a=[1,2,3,4,1,3]
b=[i for i in a]  
b.append(7)
print(f"{a}--{b}-- original list is not changed")
b=[i*i for i in a]  
print(b )

print(a.count(3))

print("--------------- practice coding questions easy-------")

print("sum all the items of a list")
li=[1,2,6,4]
summ=0
multiply=1
print(sum(li))
#another method
for i in li:
    summ+= i
    multiply*= i
print(summ,multiply)

print("-----largest from the list----")
print(max(li))
print(min(li))
#another method
large = li[0]
small = li[0]
for i in li:
    if i > large:
        large= i
    if i < small:
        small = i   
print(large, small) 


sample=['abc','xyx','aba','12321']
counti=0
for i in sample:
    if len(i)>2 :

        if i[0:1] == i[-1]:
            counti += 1
print(counti)



#remove duplicate from sorted list and add zero at the end 
alist=[1,1,1,2,2,2,3,3,4,5,5,6,8,8]
outpt=[1,2,3,4,5,6,8,0,0,0,0,0,0]
al=len(alist)
p=0
q=1
while q<al:
    if alist[p] != alist[q]:
        p+=1
        alist[p]=alist[q]
    q+=1
print(alist)    
for i in range (p+1,al):
    alist[i]=0
print(alist)  

# find all th pairs in a list that will add upto X
list4=[1,2,3,6,2,7,8]
X=10
res=[]
list4.sort()
print(list4)
i,j=0,len(list4)-1
while i<j:
    curr=list4[i]+list4[j]
    if curr==X:
        res.append((list4[i],list4[j]))
        i+=1
        j-=1
    if curr<X:
        i+=1
    if curr>X:
        j-=1
print(res)        

#Find the Closest Pair from Two Sorted Arrays:
#Given two sorted arrays, find the pair of elements (one from each array) whose sum is closest to a given value (X).

# arr1 = [1, 4, 5, 7]
# arr2 = [10, 27, 30, 40]
# X = 32  
# i,j = 1,len(arr2)-2

# currsum=arr1[0]+arr2[len(arr2)-1]
# minsum=abs(currsum-X)
# mini=minsum
# pairs=[]

# while i<len(arr1) and j>=0:
#     currsum=arr1[i]+arr2[j]
#     minsum=abs(currsum-X)

#     if minsum<mini:
#         mini=minsum
#         pairs=[(arr1[i],arr2[j])]
#     if minsum==mini:
#         pairs.append((arr1[i],arr2[j]))
#     if currsum <X:
#         i+=1
#     if currsum>X:
#         j-=1
# print(pairs)            

# arr1 = [1, 4, 5, 7]
# arr2 = [10, 27, 30, 40]
# X = 32

# # Initialize pointers
# i, j = 0, len(arr2) - 1
# pairs = []

# # Initialize the minimum difference
# currsum = arr1[0] + arr2[len(arr2) - 1]
# minsum = abs(currsum - X)
# mini = minsum

# while i < len(arr1) and j >= 0:
#     currsum = arr1[i] + arr2[j]
#     minsum = abs(currsum - X)

#     if minsum < mini:
#         mini = minsum
#         pairs = [(arr1[i], arr2[j])] #resettong the pairs each time
#     elif minsum == mini:
#         pairs.append((arr1[i], arr2[j])) #appending when sure
    
#     if currsum < X:
#         i += 1
#     else:
#         j -= 1

# print(pairs)






