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
            