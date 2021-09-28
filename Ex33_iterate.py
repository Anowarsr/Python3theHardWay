numbers=[]
def iterate(iteration, inc):
    for i in range (0, iteration):
        print(f"At the top i is {i}")
        numbers.append(i)
    # i=i+1
        print("numbers row:",numbers)
        print(f"At the bottom i is {i}")

iterate(10,4)

print("The numbers" )
for num in numbers:
    print(num)


