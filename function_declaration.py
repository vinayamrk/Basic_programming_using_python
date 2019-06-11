def f(x):
    return(x*x)
    
def greet():
    print("hello world")
    
def avg(a,b):
    return((a+b)/2)
    
    
def circle(r):
    """return the area and perimeter of circle given radiusr"""
    pi=3.14
    area=pi*r*r
    perimeter=2*pi*r
    return(area,perimeter)
    
    
def something():
    return 1,2
    
    
round(2.484)
round(2.435,2)

def welcome(greet,name="world"):
    print(greet,name)
    
    

def change(q):
    q=10
    print(q)
    
    

n=5

def change():
    n=10
    print(n)
    
n=5

def scope():
    print(n)
  

def change():
    global n
    n=10
    print (n)
      
      
name=["mr.","Steve","gosling"]

def change_name():
    name[0]='Dr.'
    
: n=5

def change(n):
    n=10
    print(n,"inside")
    

name=["mr.","Steve","gosling"]

def change_name(x):
    x={1,2,3}
    print(x,'in change')
    
def what(n):
    i=1
    while i*i<n:
        i+=1
        return i*i==n,i
        

def what(x,n):
    if n<0:
        n=-n
        x=1.0/x
    z=1.0
    while n>0:
        if n%2==1:
            z*=x
        x*=x
        n//=2
    return z
 
    
 
def f():
    def g(x):
        return x+1
    return g
    
 i/p:func=f() or f()(1)  
 
 
def f(x):
    def g(x):
        return x+1
    return g(x)**2
    
 x=['APPLE','MANGO','BANANA']
 
def to_lower(d):
    res=[]    
    for i in d:
        res.append(i.lower())



def fib(n):
    a,b=0,1
    res=[0]
    for i in range(n-1):
        res.append(b)
        a,b=b,a+b
    return(res)
    
def power2():
    def g(x):
        return (2**x)
    return g
    
    
def apply(f,data):
    res=[]
    for x in data:
        res.append(f(x))
    return res