def largest(f):
    data=[]
    for line in f:
        for field in line.split():
            data.append(float(field))
    return data
    


f=open('pendulum.txt')
out=open('col2.txt','w')
for line in f:
    fi=line.split()
    out.write(fi[1]+'\n')
f.close()
out.close()


f=open('pendulum.txt')
out=open('col2.txt','w')
for line in f:
    fi=line.split()
    print(fi[1],file=out)
f.close()
out.close()


f=open('pendulum.txt')

f1=open('col2.txt')

f2=f1.read()

f2
len(f2)
f2[0]
f2[1::2]

def my_sum(a):
    x=a.split(' ')
    l=[]
    l.append(x)
    print(l)
    
def my_sum(s):
    total=0
    for word in s.split():
        try:
            total+=int(word)
        except ValueError:
            pass
    return total
    
    
def safe_run(f,x):
    try:
        f(x)
    except ValueError:
        return 'Valueerror'
    except TypeError:
        return 'typeerror'
    else:
        return 'ok' 

def f(x):
    return x*x;

safe_run(f,3)
safe_run(f,'jghf')
safe_run(f,3.000)

def func(x):
    try:
        if x>0:
            return 'ok'
    except ValueError:
        return 'ValueError'
    except TypeError:
        return 'TypeError'
        
def func(x):
    if type(x)!=int:
        raise TypeError('Excepted int')
    elif x<0:
        raise ValueError('got negativr int')
            























