#Simple Function

def greet():
    print("Hello, Code Builder!")

#prints function multiple times in the range

for i in range(10):
    greet()


#Function with parameter

def greet_name(name):
    print("Hi, " + name + "!")

greet_name("Ryan")
greet_name("Alex")


#Function with Return Value

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5,3)
print("Sum is:", total)


#Function + loop

def print_stars(count):
    for i in range(count):
        print("*", end="") #end="" means don't go to to new line
    print() # new line

print_stars(5)
print_stars(3)
