# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:04:10 2019

@author: khali
"""
import queue

import time , threading

def factorial(x):
    a = 1
    while x >= 1:
        a = a * x
        x = x - 1
    return a
Q = queue.Queue()

y=0
num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))
a = time.time()
t1 = threading.Thread(target=lambda q, arg1: q.put(factorial(arg1)), args=(Q, num1))
t2 = threading.Thread(target=lambda q, arg1: q.put(factorial(arg1)), args=(Q, num2))
t1.start()
t2.start()
t1.join()
t2.join()
b = time.time()
while not Q.empty():
    result = Q.get()
    y=y+result
print (y)
    
print("time consumed in multithreading:\n",b-a)
