
#To make this basically you have 
#to count letters of "true" and "love" in the name of both person 
#And combine them to get you love score 




print("            ------Welcome to love calculator------")

print()
print()
print()


name1 = input("Write your name ::: ")
print()

name2 = input("Write their name ::: ")
print()

combined_name = (name1 + name2).lower()

t = combined_name.count("t")

r =  combined_name.count("r")

u =  combined_name.count("u")

e =  combined_name.count("e")

l =  combined_name.count("l")

o =  combined_name.count("o")

v =  combined_name.count("v")

e =  combined_name.count("e")

count_true = t+r+u+e

count_love = l+o+v+e

LOVE_SCORE = str(count_true)+str(count_love)



print(f"Your love score is {LOVE_SCORE}")
