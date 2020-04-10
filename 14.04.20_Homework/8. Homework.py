a=[]
if len(a)!=0:
    big=max(a)
    small=min(a)
else:
    big=0
    small=0
total=((big+small)/2)*big
missing=total-sum(a)
if missing==0:
    missing=big+1
print(missing)