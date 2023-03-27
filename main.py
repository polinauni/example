# Exercise 1
# 1.1
name = input("What's your name?")
age = input("How old are you?")
print(f"Hello {name}. Your age is {age} years old")

#1.2
x = 10
y = 15
temp = x
x = y
y = temp
print(x)
print(y)

# 1.3
num1 = 6
num2 = 10
#def check_numbers (num1, num2):
    #if num1 or num2 \6:
       # print("True")
   # elif num1 and num2 \10:
       # print ("False")
   # else:
      #  print("False")
# doesn't work

#1.4
#def sum_up(num1, num2):


# 1.5
r1 = 4
r2 = 6
r3 = 7
circle_area = (r1, r2, r3)
from math import pi
print("The area of the circle with radius " + str(r1) + " is: " + str(pi * r1 ** 2))
print("The area of the circle with radius " + str(r2) + " is: " + str(pi * r2 ** 2))
print("The area of the circle with radius " + str(r3) + " is: " + str(pi * r3 ** 2))

#1.6
#text = apple
#def check_string(text):
#    if str(start [a]):
#        return True
#    else str(end [a])
#        return True
#text = apple
#doesn't work

#1.7
n = 4
for i in range (n):
    for j in range (i+1) :
        print("*", end="")
    print()



my_list = ['cat', 2, 3, 4]

print(my_list[0])

for i in my_list:
    print(i)








