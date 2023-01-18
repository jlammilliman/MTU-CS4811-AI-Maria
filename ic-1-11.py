import math # Math is a neat library within python

# To run a python file, open conda and activate your environment
# run:  python ./file-name.py

# To exit from python
# run:  exit()

# This is how you make comments lol
print('============================================================================================================')
print(" ==> Notes from lecture (1-11-2023) Wednesday:")
print("         Python is an interpreted language, as opposed to a compiled language like java. Java compiles to"   )
print("     byte code. Whereas python skips the compilation step and allows you to directly run the raw python code.")
print("     Integers, floating point numbers and complex numbers are all objects just floating in space. Python will")
print("     interpret variables as refernces to this free space. Functions are 'magic' black-boxes. If it takes the ")
print("     input, and you get the correct output, YOU DONE GOOD. ")
print('============================================================================================================')
x = 1    ; print("     x: ", x, type(x)) # int      
y = 2.8  ; print("     y: ", y, type(y)) # float
z = 1j   ; print("     z: ", z, type(z)) # complex
print('============================================================================================================')
print(" ==> In-Class Examples:")
print("     1) Seconds in a non-leap year: ", (365 * 24 * 60 * 60), "s" )
print("     2) Inches in a Mile: ", (5280 * 12) )                   # I totally remember how many feet are in a mile ==> 5280ft....
print("     3) Compute the number of 2ft^2 tiles to cover the floor of a 10 by 12 ft room: ", ((10 * 12) / (2 * 2)) )
print("     4) Compute the ages of five people around you: ", (21 + 23 + 25 + 20 + 19) / 5.0 )
print("     5) Compute the factorial of 13: ", math.factorial(13) ) # Import math library 
print("     6) Compute 2 to the 120th power: ", (2)**(120) )        # Exponentialize

# This is how you define a function
# Indentation has to be consistent, as python solely looks at indentation :D
def functionName(param1, param2):
    print(param1)
    print(param2)


# TURTLE TIME
import turtle

t = turtle.Turtle()
t.fillcolor("red")
t.speed(50000)
#Draw a square
for k in range(3):
    for i in range(360):
        t.forward(1)
        t.left(1)



