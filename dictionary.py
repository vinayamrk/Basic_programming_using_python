txt=input().lower()
res={}
for char in txt:
    if char in res:
        res[char]+=1
    else:
        res[char]=1
        
for char in sorted(res):
    print(char,res[char])
    
months=('jan feb mar may jun jul aug sep oct nov dec')
monthmm={}
for i,month in enumerate(months):
    monthmm[month]=i+1
    
date= input()
date=date.replace(',',' ')
day,month,year=date.split()

dd,yyyy=int(day),int(year)
mon=month[:3].lower()
mm=monthmm[mon]
print((yyyy,mm,dd))