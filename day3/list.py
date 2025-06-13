#List are one of four collections of data in python

users = ['Dave', 'john', 'Sara']

data = ['Dave', "42", "True"]

emptylist = []

print('Dave' in emptylist) #find a specific string in a list
print(users[0]) #get the index of a value in a list
print(users[-2])
str(data)
print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))  #print length of data

users.append('Elsa')   #add to a list
print(users)

users += ['Jason']  #add to a list
print(users)

users.extend(['Robert', 'Jimmy'])  #ADD TO A LIST
print(users)

users.extend(data)  #add a lis to another.
print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']  #add to a specific index in a list
print(users)

users.remove('Bob') #remove from a list
print(users)

print(users.pop())  #remove the last value from a list
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)

nums = [4, 42 ,78, 1, 5]
nums.reverse() #the list in reverse order.
print(nums)

#to sort numbers in ascending order

# the particular method below sorts the original list:
#nums.sort(reverse=True)
#print(nums)

#This list sorts the value one time and retains the original value.
print(sorted(nums, reverse=True))
print(nums)


#another way is to make a copy, sort the copy and run the print command.
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort() #sorted the copy of the list
print(mycopy)
print(nums)

print(type(nums)) 

mylist = list([2, "list", True])
print(mylist)


#tuples are very much like lists except the data will not change

mytuple = tuple(('Dave', 42, True))  #creating a tuple

anotherTuple = (1,4,2,8,2,2)  #creating a tuple

print(mytuple)

print(type(mytuple))
print(type(anotherTuple))

#appending a list with a tuple or packing
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(2))