name = "Dave" #global scope which is defined outside of a function can be referenced within a function.

count = 1

#calling another function that is defined within a global scope.
def another():
    color ="blue"

#to modify a global variable or value we can add the "global" keyword to it.
    global count
    count += 2
    print(count)
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("dave")

another()

#we can try not to pollute our code with many functions and variables.
#we can do that using nested functions and have them scoped inside of a function.

