name =input("Please enter your name: ")
age =int(input("How old are you, {0} ? ".format(name)))
print (age)

if age >=18:
    print("you can vote")
else:
    print("Please comeback in {0} years".format(18-age))
print("-" *100)
age =2
if age >2:
    print("age is greater than 2")
elif age ==2:
    print("age is 2")
else:
    print("age is less than 2")

print("_"*100)

age = int(input())
if age >2:
    print("age is greater than 2")
    age=int(input())
    if age==2:
        print("gussed it correctly")
elif age ==2:
    print("age is 2")
else:
    print("age is less than 2")

print("_"*100)

print("guess a number from 1 to  10: ")
a =int(input())
b=5
if a !=b:
    if a<b:
        print("guess higher")
    else:
        print("not lower")
    guess =int(input())
    if guess ==b:
        print("well done")
    else:
        print("wrong")
else:
    print("gussed it correclty first time")

print("*"*100)

age = int(input("How old are you? "))

if age>=16 and age <65:
    print("eligible to work")
else:
    print("u cant work")

print("*"*100)

age = int(input("How old are you? "))

if 16 < age <65:
    print("eligible to work")
else:
    print("u cant work")





