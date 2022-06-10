n=int(input("Enter number"))
p=int(input("Enter number 2"))
b=0
for x in range(1,n):
    if(n%x==0):
        b=b+x
        
a=0
for z in range(1,p):
    if(p%z==0):
        a=a+z

if(b==p and a==n):
    print("True")
    
else:
    print("False")
        
        
  
        
        
      
        
        