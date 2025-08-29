#dictionaries are used to store data that are in key value pairs
band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocals="Plant", guitar="Page") # define a dictionary 

print(band)
print(band2)
print(type(band))
print(len(band))

#access items
print(band["guitar"])
print(band.get("vocals"))

#list all keys in a dictionary.
print(band2.keys())

#list all values

print(band.values())

#list all key/value pairs as tuples
print(band.items())

#verify if a key exists
print("guitar" in band)
print("triangle" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass":"jpj"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear

band["drums"] = "Bonham"

del band["drums"]
print(band)

band2.clear()
print(band2)
del(band2)

#copy dictionaries

# band2 = band  #creates a reference not copy.
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["drums"] = "dave"
# print(band)
# print(band2)
print("Good copy")
band2 = band.copy()
band2["drum"] = "Dave"
print(band)
print(band2)

#make a copy using the dict() constructor function
band3 = dict(band)
print("good copy")
print(band3)
# print(band3)
# band["artist"] = "rema"
# print(band3)

member1 = {
    "name": "plant",
    "instrument": "guitar"
    }
member2 = {
    "name": "page",
    "instrument" : "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

#sets

nums = {
    1,2,3,4
}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicate
nums = {1,2,3,2}
print(nums)

#True is a dupe of 1, False is a dupe of zero
nums = {1, True,2,False,3,4,0}
print(nums)

#check if a value is in a set

print(2 in nums)

#but you cannout refer to an element in the set with an index position or key.

#add a new element to a set.

nums.add(8)
print(nums)

#add elements from one set to another.
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries too.


# merge two sets to create a new set.

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

#keep only duplicates
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)

#keep everything except duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)


