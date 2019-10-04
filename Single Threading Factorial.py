import time , threading

def factorial(x):
    a = 1
    while x >= 1:
        a = a * x
        x = x - 1
    return a


num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

a = time.time()
print("sum of factorials= \n",factorial(num1)+factorial(num2))
b = time.time()

print("time consumed in single thread:\n",b-a)

