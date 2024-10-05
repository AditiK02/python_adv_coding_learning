#key-value pairs, unorderd, mutable
mydict1={"name": "adk","age":23,"city":"Banglore"}
print(mydict1)

mydict2= dict(name="ak",age=21,city="IXE")
print(mydict2)

value = mydict1["name"]
print(value)

mydict1["email"] = "cool@xyz.comS"
print(mydict1)
mydict1["email"] = "notcool@xyz.com"  #overwritten value
print(mydict1)

if "name" in mydict1:
    print(mydict1["name"])


for key in mydict2:
    print(key)   

for x in mydict2.values():
    print(x)    
for x in mydict2.keys():
    print(x) 

for i,j in mydict1.items():
    print(i,j)    


#copying a dictionary
mydict1_cpy= mydict1  # wrong way to copy one dict to another
mydict1_cpy["name"] = "galu"
print(mydict1)
print(mydict1_cpy)

#correct way to copy
mydict1_cpy= mydict1.copy()  #or mydict1_cpy= dict(mydict1)
mydict1_cpy["name"] = "galu"
print(mydict1)
print(mydict1_cpy)

mydict2.update(mydict1_cpy)
print(mydict2)



mystr="i am a girly girli"
print(mystr)
mylist=mystr.split()
print(mylist)
#first method
longest = ""
for word in mylist:
    if len(word) > len(longest):
        longest = word
        count = len(longest)
print(longest,":",count)
#second method
dict1=dict()
for i in mylist:
    dict1[i]=len(i)
print(dict1)
maxval=max(dict1.values())
for key,val in dict1.items():
    if val==maxval:
        print(key,":",val)
        


li=["as","bv"]
for i in range(1):
    print(li[i],li[i+1])