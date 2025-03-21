# HERE WE ARE TRYING TO UNDERSTAND ERRORS AND EXCEPTIONS IN PYTHON 
# WE WILL TRY TO CREATE SOME EXCEPTION HERE

# KEY ERROR
# (so this error occurs in case of dictionary, basically while trying to access the key which is not there in the key-value pairs)
dic1={'name':"Ak",'age': 24}
# print(dic1['college'])  it raises key error
try:
    print(dic1['college'])
except KeyError as e:
    print(f"Key error occured :{e}")    




# ATTRIBUTE ERROR
class pet:
    def __init__(self,dog):
        self.dog=dog

p=pet("tommy_dog")        
#print(p.cat)  raises attribut error cuz no 'cat' attribut exists in pet object
try:
    print(p.cat)
except AttributeError as e:
    print(f"Attribute error occured : {e}")    

#-----------------------------------------------------------
#Attribute error also occurs when instance attribute is accessed as class attribute
#-----------------------------------------------------------
class Pet:
    species = "Animal"  # Class attribute

    def __init__(self, dog):
        self.dog = dog  # Instance attribute

p1 = Pet("tommy_dog")
p2 = Pet("rocky_dog")

# Accessing the class attribute
print(Pet.species)  # Output: Animal (accessing class attribute using class name)
print(p1.species)   # Output: Animal  (accessing class attribute using instance p1)
print(p2.species)   # Output: Animal   (accessing class attribute using instance p2)
print(p1.dog) # Output: tommy_dog (accessing instance attribute)

#print(Pet.dog) # Will generate Attribute error
try:
    print(Pet.dog)
except AttributeError as e:
    print(f"Attribute error occured : {e}")  



#VALUE ERROR
#age=int(input("Enter your age"))  Raises value error if non integer value, such as ;"abg","2s"
try:
    age=int(input("Enter your age"))
except ValueError as e:
    print(f" Value Error occured :{e}")


#TYPE ERROR
# Occurs when different type than expected type is entered
#b="5" + 5   TypeError: Can't concatenate a string and an integer.
try:
    b="5" + 5 
    print(b)
except TypeError as e:
    print(f"Type Error occured :{e}")


#INDEX ERROR
#occurs when trying to access index which does not exist in the list
li1=[1,2,3,4,5]
print(f"printing index: {li1[4]}")
#print(li1[10])  LIST INDEX OUT OF RANGE ERROR
try:
    print(li1[10])
except IndexError as e:
    print(f"INDEX Error occured :{e}")



#FILE NOT FOUND ERROR
file1 = open('filetry.txt')
file1.close()
file1=open('filetry.txt')
file1.seek(0) # Bring file cursor to initial position.
print(file1.read())
file1.close()   # file closed normally

#File not found case1
try:
    f2=open('fil.txt','r') #throws error cuz no file named fil.txt exists
    f2.read()
    f2.close()
except FileNotFoundError as e:
    print(f"FileNotFoundError occured :{e}")

#case2
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()  # File doesn't exist
except FileNotFoundError as e:
    print(f"FileNotFoundError occured :{e}")




#RUNTIME ERROR
#here it will raise 'recursion error'
#'recursion error is the subtype for runtime error
def recursive_function():
    return recursive_function()  # No termination condition

recursive_function()

