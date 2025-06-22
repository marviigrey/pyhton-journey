#defining a function

def hello():
    print("hello world")

hello()

def sum(num1=0, num2=0):
    if type(num1) != int | type(num2) != int:
        return 0
    return num1 + num2

total = sum(7, 8)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "john", "Sara")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first = "Dave", last="gray")