#!/usr/bin/python

# I want put in a number that gives how many fibonacci numbers I get out

print ("How many fibonancci numbers?")
n = input('Enter the number here: ')


# I got to have the fibonacci equasion

# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
	return ""
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
# Driver Program





i = 1
fiblist = []
if n <= 0:
	print("Incorrect Input")
if n >= 35:
	print("This is too intense for this weak ass computer")
else:
	while i <= n:
		fiblist.append(Fibonacci(i+1))
		i = i + 1
	print (fiblist)	
 
	
print("This was added at home")

