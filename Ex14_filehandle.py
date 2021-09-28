from sys import argv

script,User_name = argv
promt = '>'

print(f"Hi I'm {User_name}.I'm good in {script}")
print(f"You Know my name!{User_name}")

print("Just put a name: ")
tags = input(promt)

print("Which type of laptop you have?")
laptop = input(promt)
print("Where is your Hometown?")
hometown = input(promt)

print(f'''Okay!! you said that {tags} know about me, 
currently you have {laptop} laptop 
and you said to me that your hometown is {hometown}.
It is a great,have a good day!!''')