 c=3+4j
 dtype
 t=True

F= not t

F or t


F and t


a=False

b=True

c=True

(a and b) or c


a and (b or c)


a and b or c

print("this is cool")


print("""this is cool""")


w='hello'

print(w[0],w[1],w[-1])

len(w)

a=1.0

type(a)


type(1)


type(1+1j)




type(c)


1786%12


45%2


8646
big=1234567891234567890**3

big
Out[33]: 1881676377434183981909562699940347954480361860897069000

verbig=big*big*big*big

verbig
Out[35]: 12536598903329366187366602453637834523513900340514681990694177938853001286963089597513186328270383939298923641110340456447058221912767480641620897695065961403207129435677004066945018482594529234494366959121000000000000

31240*126789
Out[36]: 3960888360

17/2
Out[37]: 8.5

17
Out[38]: 17

170/2.0
Out[39]: 85.0

17.0/2
Out[40]: 8.5

17.0/8.5
Out[41]: 2.0

c=3+4j

abs(c)
Out[43]: 5.0

c.imag
Out[44]: 4.0

c.real
Out[45]: 3.0

c.conjugate()
Out[46]: (3-4j)

a=7546

a+=1

a
Out[49]: 7547

a-=1

a
Out[51]: 7546

a*=1

a
Out[53]: 7546

a/=1

a
Out[55]: 7546.0

s='hello'

p='world'

s+p
Out[58]: 'helloworld'

s*4
Out[59]: 'hellohellohellohello'

s*s
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-60-35e6e2387f23> in <module>()
----> 1 s*s

TypeError: can't multiply sequence by non-int of type 'str' 

a='hello world'

a.startswith('hell')
Out[62]: True

a.endswith('ld')
Out[63]: True

a.upper()
Out[64]: 'HELLO WORLD'

a.lower()
Out[65]: 'hello world'

b=a.strip()

b
Out[67]: 'hello world'

b.index(ll)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-68-1454345f69e5> in <module>()
----> 1 b.index(ll)

NameError: name 'll' is not defined 

b.index(ll)

b.index(ll)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-70-1454345f69e5> in <module>()
----> 1 b.index(ll)

NameError: name 'll' is not defined 

b
Out[71]: 'hello world'



b.index(ll)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-72-1454345f69e5> in <module>()
----> 1 b.index(ll)

NameError: name 'll' is not defined 

b.index('ll')
Out[73]: 2

b.replace('hello','goodbye')
Out[74]: 'goodbye world'

chars='a b c'

chars.split()
Out[76]: ['a', 'b', 'c']

''.join(['a','b','c'])
Out[77]: 'abc'

alpha =','.join(['a','b','c'])

alpha
Out[79]: 'a,b,c'

alpha.split(', ')
Out[80]: ['a,b,c']
