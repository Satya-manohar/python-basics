n=int(input("enter number "))
x=n**2
num1=0
while(n>0):
    r=n%10
    num1=num1*10+r
    n=n//10
    y=num1**2
num2=0
while y>0:
    p=y%10
    num2=num2*10+p
    y=y//10
if x==num2:
    print("True")
else :
    print("False")