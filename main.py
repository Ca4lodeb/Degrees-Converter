# Made by @carlo.deb on TikTok | ca4lo.deb on IG
# Celsius to Fahrenheit or Fahrenheit to Celsius
import time

# Try
try:
# Welcoming
    print("Hello! Welcome to the program were you can convert Celsius to Fahrenheit and Fahrenheit to Celsius!")

# Adding a delay between the two functions
    time.sleep(2)

# c to f
        # C to F
    C = float(input("What is your temparature in Celsius?\n"))
    F = (C * 9/5) + 32
    print('%.2f Degrees Celsius is: %0.2f Degrees in Fahrenheit' %(C, F)) # Credits to https://beginnersbook.com/2019/05/python-program-to-convert-celsius-to-fahrenheit-and-vice-versa/ for this line of code


# f to c
    F2 = float(input("What is your temparature in Fahrenheit?\n"))
    C2 = (F2 - 32) * 5/9
    print('%.2f Degrees Fahrenheit is: %0.2f Degrees in Celsius' %(F2, C2)) # Credits to https://beginnersbook.com/2019/05/python-program-to-convert-celsius-to-fahrenheit-and-vice-versa/ for this line of code

# Except
except:
    print("Goodbye!")
