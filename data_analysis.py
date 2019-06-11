import numpy as np
data=[1.0,4.5,2.3,-0.5,0.5,2.8]
np.mean(data)
np.median(data)
np.std(data)
np.var(data)
data.sort()

data


md=np.arange(16)

md.shape=4,4

md
np.mean(md)
np.std(md)
np.mean(md, axis=0)
np.mean(md, axis=1)
np.NaN
np.NaN+1
np.inf
np.inf+1
data=[1.0,2.1,np.nan,3.0]
np.mean(data)
np.std(data)
np.nanmean(data)
np.nanstd(data)
data=np.random.random(5)
x=np.random.random((3,3))
x.shape
np.random.randint(-5,10,size=5)
np.random.normal(loc=0.0,scale=1.0,size=5)


data=np.random.normal(size=1000)
from matplotlib import pyplot as plt
plt.hist(data)


data=np.random.poisson(lam=0.5,size=10000)
ax1=plt.subplot(1,2,1)
ax1.hist(data,normed=True)
ax2=plt.subplot(1,2,2)
ax2.hist(data,cumulative=True)

for i in range(1,5):
    ax=plt.subplot(2,2,i)
    ax.text(0.0,0.5,'plot number %d'% i)
data=np.random.chisquare(7,size=1000)    
ax1=plt.subplot(1,2,1)
ax1.hist(data,normed=True)
ax2=plt.subplot(1,2,2)
ax2.hist(data, cumulative=True)
 
np.random.seed(27)
np.random.random()
 
 
data=np.random.normal(loc=10,scale=2,size=1000)
np.percentile(data,50)
np.median(data)
np.percentile(data,[25,50,75])

data=np.random.randint(0,100,size=5)
data
np.random.shuffle(data)
np.random.permutation(10)
np.random.permutation(data)

data=np.random.permutation(5)
data
np.random.choice(data)
np.random.choice(data,size=5)
np.random.choice(data,size=5,replace=False)




