# Code for Fibonachi numbers

def fib(x): # define the function
    if x == 1: # provide a base case for 1
        return 1
    elif x == 0: # provide a base case for 0
        return 0
    else:
        return fib(x-1) + fib(x-2) # add the two previous numbers from x

x= eval(input("Please Enter a number: ")) # promnt the user for a numnber
for i in range(x):
    print(fib(i), end=" ") # print the fibonachi numbers in their order



