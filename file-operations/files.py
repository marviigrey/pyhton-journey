import os
#r- Read
#s- Append
#w- write
#x- Create

#Read - error if it doesnt edit

f = open("names.txt")
#print(f.read())  #read the content of a file.
#print(f.read(4)) #read the first four characters of the file.

# print(f.readline()) #read the first line of the file.
# print(f.readline()) #read the first line of the file.

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("the file you want to read doesnt exist")
finally:
    f.close()

#Append - creates the file if it doesnt exist.
f = open("names.txt", "a")
f.write("Ziarn\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

#Write (overwrite)
f= open("context.txt", "w")
f.write("I delete all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#two ways to create a new file

#Opens a file for writing, creates the file if it doesnt exist.
f = open("name_list.txt", "w")
f.close()

#Creates the specified file but returns error if the file exists
if not os.path.exists("marv.txt"): #using the os module, if the file path doesnt exist,create it.
    f = open("marv.txt", "x")
    f.close()

#Delete a file

#avoid an error if it doesnt exist
if os.path.exists("marv.txt"):
    os.remove("marv.txt")
else:
    print("The file doesnt exist.")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
