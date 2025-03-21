#sets: unordered, mutable, no duplicates
mysets ={1,2,3,2,8.6,"rty"}
set1=set("hello") #unordered
print(set1)
print(mysets)

set2= set()
set2.add(1)
set2.add(2)
set2.remove(2)
#set2.remove(4) #will raise key error cuz 4 not present in set

set1.discard(4) # if element not found then no error, if found then removed

#mysets.clear() #empty the set
#mysets.pop(4)

for i in mysets:
    print(i)

#union and intersection

odd={1,3,5,7}
even ={0,2,4,6,8}
primes={2,3,5,7,11}

u = odd.union(even) #or use "|" for union 
print(u)

i = odd.intersection(even) #or use "&" for intersection
print(i) #emppty sets

ep = even.intersection(primes) #or use  
print(ep)

#difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,16,15,13}

diff = setA.difference(setB) # returns what in setA but not in setB
#set difference using "-"
print(diff)

sym_diff = setA.symmetric_difference(setB) # returns what in setA and setB except what is common
# cana lso use "^" for symmetric differnce
print(sym_diff)

setA.update(setB) 
print(setA)

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA.issubset(setB))

print(setA.issuperset(setB))

a=len(setA)
print(a)

#PRACTICE QUESTION

# 1. size of set 
import sys
setA = {1,2,3,4,5,6}
print(sys.getsizeof(setA),"bytes") #getsizeof in sys module
print(set1.__sizeof__(),"bytes")

# 2. Example set
my_set = {10, 20, 30, 40, 50}

# Enumerated for loop over the set
for index, value in enumerate(my_set):
    print(f"Index {index}: {value}")

#3. max and min in sets
print(max(setA))
print(min(setA))


#4. if 3 list have atleast one element common
def commom(a,b,c):
    aset=set(a)
    bset=set(b)
    cset=set(c)
    if aset & bset & cset:
        return True
    else:
        return False

a=[1,2,4,'a']
b=[2,3,5,'a']
c=[9,10,2]
print(commom(a,b,c))

#5. missing and additional valus in two list
a=[1,2,4]
b=[2,3,5]
def missing_additional(a,b):
    aset=set(a)
    bset=set(b)
    mi_li1=bset-aset
    mis_li2=aset-bset
    add_li1=aset-bset
    add_li2=bset-aset
    return mi_li1, mis_li2, add_li1, add_li2
mi_li1, mis_li2, add_li1, add_li2 = missing_additional(a,b)
print(mi_li1, mis_li2, add_li1, add_li2)

# 6. difference between two list
# or can say present in one list but not in other

li1=[1,2,4,6]
li2=[2,3,7,8]
#output = [1,4,6]
temp=[]
for i in li1:
    if i not in li2:
        temp.append(i)
print(temp)        

#another method --set()
s_li1 = set(li1)
s_li2 = set(li2)
diff_li1=s_li1 - s_li2
print(list(diff_li1))

# 7. lost array from duplicated array
li1=[1,2,4,6]
li2=[1,2,4,6,8]
s_li1 = set(li1)
s_li2 = set(li2)
if len(s_li1)>len(s_li2):
    print(s_li1-s_li2)
else:
    print(s_li2-s_li1)    

# 8. count vowels using sets in a given string
vowel=set("aeiouAEIOU")
string="aditi"
srt_set=string
count=0
for i in srt_set:
    if  i in vowel:
        count+=1
print(count)        

# 9. accept the strings which contain all vowels

vowel=set("aeiou")
string = "adJKitioue"
s=set()
string= string.lower()
for i in string:
    if i in vowel:
        s.add(i)
if len(s) == len(vowel):
    print("accepted")
else:
    print("not accepted")

# 10.  check if given string is binary string or not
binary= set("01")
s=set()
strin="11110600101"
for i in strin:
    if i not in binary:
        s.add(i)
print(s)       
if not s: #checks if set is empty or not
    print("yes")
else:
    print("no")    

#11. panagram or not
import string
print(string.ascii_lowercase) #get all the alphabet in lowercase 
ailphbet=set(string.ascii_lowercase)
by= "The quick brown fox jumps over the lazy dog."

if ailphbet-set(by) == set():
    print("panagram")
else:
    print("not panagram")    

#12.    