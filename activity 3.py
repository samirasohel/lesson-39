#Write a Python program to check whether a number entered by the user is greater than 50 or not.
#  Also, if it is greater than 50, then check whether it is odd or even.

num=int(input("Enter a number"))

if num > 60:
    print(num,"is greater than 60")
    #nested if
    if num%2==0:
        print("and this is a even number")
    else:
        print("and this is a odd number")
else:
    print(num,"is less than 60")