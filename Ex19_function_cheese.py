def cheese_cracker(ch_count, cr_count):
    print(f"You have {ch_count} cheese")
    print(f"You have {cr_count} no boxes of crackers")
    print("mans that enough for party")

print("We can just give the function numbers directly:")
cheese_cracker(20,30)

print("Or we can use variables from our script:")
amount_cheese=10
amount_cracker=20

cheese_cracker(amount_cheese, amount_cracker)

print("we can even do math inside too")
cheese_cracker(10+20,5+6)

print("we can combine two math and variables:")
cheese_cracker(amount_cheese+10000,amount_cracker+2000)
