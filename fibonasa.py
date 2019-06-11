n=int(input("enter the n:"))
a,b=0,1

while b <n:
    print(b,end=' ')
    next=a+b
    a=b
    b=next
    
while b<500:
    if b%4 == 0:
        print(b)
        break
    a,b=b,a+b
    
for n in range(1,10,2):
    if n%3==0:
        continue
    print(n+n)
    
    