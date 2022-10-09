
num=int(input("enter a number:"))

a=0
b=1
s=0

for i in range(num):
    print(s,end=" ")
    s=a+b
    b=a
    a=s