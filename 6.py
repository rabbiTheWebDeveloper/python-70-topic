# and or not 
print (10+5 and 5+5) # and operator
print (10+5 ==6 or 5+5 ==6) # or operator
print (not(10+5)) # not operator
# precedence
mark = 58
if mark >= 80 and mark <= 100:
    print("A+")
elif mark >= 70 and mark < 80:
    print("A")
elif mark >= 60 and mark < 70:
    print("A-")
elif mark >= 50 and mark < 60:
    print("B")
elif mark >= 40 and mark < 50:
    print("C")  
elif mark >= 33 and mark < 40:
    print("D")