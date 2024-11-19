#Write a Python program that takes height and weight as an input from the user,
#  calculates BMI and, based on the value of BMI,
#  displays the resultant category in which the user falls.

height=int(input("Enter a height"))
weight=int(input("Enter a weight"))

bmi=weight/(height/100)**2

if bmi <=24.9:
    print("You are underweight")
elif bmi <=29.9 :
    print("You are healthy")
elif bmi <=34.9:
    print("You are overweight")
elif bmi <=39.9:
    print("You are severly overweight")
elif bmi <=44.9:
    print("you are obese")   
else:
    print("you are severly obese")