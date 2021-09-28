def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# num = 4
num = int(input("Enter a number to find its factorial: " ))
print("The factorial of", num, "is", factorial(num))