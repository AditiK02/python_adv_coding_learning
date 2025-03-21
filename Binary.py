#Convert Binary to integer
n=int('1001',2)
print(type(n),n)

#convert integer to binary
z= 2
print(bin(z),) #since first two digits represent bin form, we do slicing
b=bin(z)[2::]
print(b)

# Add/sub/mul/div WITHOUT using arithmetic operator (+,-,,*,%)

#USING operator module

import operator as op
print(op.__all__) #'.__all__' to view all the function in the module
a,b=5,2
c=-8.9
print(op.add(a,b))
print(op.sub(a,b))
print(op.mul(a,b))
print(op.truediv(a,b))
print(op.floordiv(a,b))
print(op.pow(a,b))
print(op.abs(c)) #gives absolute value eg. abs(-4) is 4

#But operator module internally use (+-*/)
#so we will use bit wise operator

#---- SUM without carry
print(a^b) # correct cuz no carry, small numbers

print(56^43) # WRONG answer cuz carry forward , big numbers
#---- SUM with Carry
a,b=56,43
while b!=0:
    sum=a^b
    carry=(a&b)<<1
    a=sum
    b=carry
print(a)