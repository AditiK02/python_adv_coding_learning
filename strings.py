# Strings: ordered, immutable, text representation
# % , format() , f-Strings
mystr = "hello"
mystr1 = 'aditi'
mystr2 = """ hello
bye it is used to create multiline string with
out having actual line in output
basically used for documentation purposes"""

mystrsub = mystr[1:2]
mysub = mystr[::-1]
concat = mystr + mystr1

for i in mystr1:
    print(i, end=" ")

if 'a' in mystr1:
    print("a is present")

print(mystr1.upper())
print(mystr1.lower())

print(mystr1.find('o'))
print(mystr1.count('o'))
print(mystr1.replace('ad','ob'))


str1= "he yu hii"
list1= str1.split(" ")
print(list1)

newstr=' '.join(list1)
print(newstr)

# % method
var = 4.56
a= 89
str6 = "the variable ia %d " % var
print(str6)

# format() method
str6 = "the variable ia {} ".format(var)
str6 = "the variable ia {} and {} ".format(var,a)
print(str6)

# fstrings
str6 = f"the variable ia {var} and {a}"
print(str6)
