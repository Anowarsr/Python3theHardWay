ten_things="Apples Oranges Crows Telephone Light Sugar"
print("Wait there")

stuff= ten_things.split(' ')
more_stuff=("Day","Night","Song","Frisbee","Girl","Boy","Corn","Banana")

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)}")

print("There we go: ",stuff)
print("Lets do some thing")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
