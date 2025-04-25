
weight=input("Write your weight(kg) :  ")
height = input("write your height(m)  :  ")

#input function always give string so convert in integer 

X=int(weight)
Y=int(height)

bmi=str(X/Y**2)

# we need to convert x/y**2 in str because we can't cacenate integer with string see next step'

print("Your body mass index(bmi) is = " +bmi)

#alternate
#bmi=X/Y**2
#print("Your body amss index(bmi) is = " + str(bmi))
