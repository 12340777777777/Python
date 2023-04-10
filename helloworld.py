print('hello')
print("hello" + "hello")
greeting = "hello"
name ="1"
print(greeting + ' ' + name) #gives error for int
g=input("Enter name ")
print(greeting + ' ' + g) #gives error for int

#escape charecters
splitString = "This spring has been\nsplit\nsplit"
print(splitString)

tabbedString ="1\t2\t3\t4"
print(tabbedString)

#writing special characters
print('The pet shop owner said "No, no \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no 'e's uh,...he's resting\".")
print("""The pet shop owner said "No, no 'e's uh,...he's resting".""")

another="""s
d
d
d"""
print(another)
another="""s
d\
d\
d"""
print(another)

print(12//4) #integer rounded

z ="pyhton"
print(z[3])
print(z[0:4])
print(z[0:6:2]) #in steps of 2 excludes 6
number ="9,226,456,456,565,555"
print(number[1::4])#starts with 1st value and slices every 4th character

#slicing backwards
letters="wedewfregrgtrhthth"
print(letters[10:0:-1])#reverse order except 1, b[::-1} this does it
print(letters[:-9:-1]) #last 8 in reverse order
print(z[-4:]) #last4 values
print("a" *5)

print("There are {0} days in {1}, {2}, {3}".format(31, "Jan", "Mar", "Feb"))
f ="friday"
print("day" in f)
print("hi" in f)

age=24
print("age is {0} years".format(age))

for i in range(1,13):
    print("NO {0} is sqred and no {1} is cube". format(i**2, i**3))

age =2
print(name+f" is {age} years old")

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])