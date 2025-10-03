# 

#new method 
a=input()
len_a=len(a)
sum=0
for i in a :
    sum = sum+ int(i)**len_a
if int(sum)==int(a):
    print("Armstrong")
else:
    print("Not Armstrong ")