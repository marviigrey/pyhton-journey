squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum_total = lambda a, b : a + b

print(sum_total(2,5))
########################################
def funcBuilder(x): 
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(4))
print(addTAwenty(5))

###############################
# a higher order function returns a function as an argument or recieves a function as an argument.

lambda num : num * num
numbers = [3, 4, 6, 23, 65, 32]
squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))
#we used lambda and map() function [line 25-27] to achieve the loop [line 31-33]
#for x in numbers:
 #   square = x * x
  #  print(square) 

#####################################
lambda num : num % 2 != 0

odd_num = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_num))

from functools import reduce

lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)
print(sum(numbers, 20))

lambda acc, curr: acc + len(curr)

names = ['marviigrey', 'justin gale', 'Sara Ito', 'john doe']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)