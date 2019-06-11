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
    
    