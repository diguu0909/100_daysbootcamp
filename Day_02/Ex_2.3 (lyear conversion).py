

#Suppose you have to live for 90 years then write a program  to calculate your life left in years ,months ,days
#assumption's no leap year 





age = input("what's your age in years :  ")

age_left = 90 - int(age)

days = age_left*365

years =age_left

weeks =52*years

print(f"you have {days} days , {weeks} weeks , { age_left} years")

# you can also do this using concatenation
