s=input()
n=s.lower()
a='aeiou'
count=0
for i in a:
    if i in n:
        count=count+ 1
if count==5:
    print("True")
else:
    print("False")