i=0
num=[]
while i<6:
    print(f"At the top i is {i}")
    num.append(i)
    i=i+1
    print("numbers row:",num)
    print(f"At the bottom i is {i}")

print("The numbers" )
for numbers in num:
    print(numbers)