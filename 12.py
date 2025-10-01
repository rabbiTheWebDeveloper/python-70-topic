year=int(input("Enter your year : "))

if year % 4==0 or year % 400==0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is not a leap year")
else:
    print("This is not a leap year")