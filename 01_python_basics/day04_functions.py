# Day 4 : Functions in Python
# 1. Simple function
def greet():
    print("hello, Engineer!!")

greet()

# 2. functions with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Sumit")    

# 3. functions with return Value
def add_numbers(a,b):
    return a + b
result = add_numbers(10,20)
print("sum:", result)

# 4. even or odd checker
def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"  
num=int(input("enter a  number:"))
print("the number is :", check_even_odd(num))      

