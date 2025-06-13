#string data type

#literal assigment:

first = "marvii"
last = "grey"

# print(type(first)) #check if the data type.
# print(type(first)== str) # check if data type is string.
# print(type(first)== str) # check if data type is string.

print(isinstance(first, str))

#construction function

pizza = str("pepperoni")
print(type(pizza))
print(type (pizza) == str)
print(isinstance(pizza, str))


#concatenation
fullname = first + " " + last 
print(fullname)


#casting a number to string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I love afrobeats music from the " + decade + "s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just checking in, 

                            all good?

'''
print(multiline)

#escaping special character

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                 "
multiline = "               " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
#build a menu

title = "menu".upper()
print(title.center(20, "."))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("doughnuts".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$1.5".rjust(6))



print("")

#index value
print(first[1])
print(first[-1]) #to get the last letter in a string
print(first[1:])


#some methods return boolean
print(first.startswith("m"))
print(first.endswith("Z"))


#boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


#Numeric data types

#-----Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#----float type

gpa = 3.2
y = float(1.15)
print(type(gpa))
print(isinstance(y, float))

#-----complex type

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#builtin number functions
print(abs(gpa))

print(round(gpa))

print(round(gpa, 1))

print(abs(gpa * -1))

import math

print(math.pi)

print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode = "100263"
zip_value = int(zipcode)
print(type(zip_value))