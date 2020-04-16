l=[101, 110, 220, 100, 103, 606, 603]
def repeat(l):
    a=[]
    k=list(map(str,l))
    for i in range(len(k)):
        if len(set(k[i]))==len(k[i]):
            a.append(k[i])
    if len(a)!=0:
        return int(a[0])
    else:
        return -1

print(repeat(l))
