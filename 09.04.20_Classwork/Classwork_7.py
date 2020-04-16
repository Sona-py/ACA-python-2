l=[1,2,3]
l1=[3,2,1]
a=[]
def circular(l,l1):
    for i in l:
        if l[i:]+l[:i]==l1:
            a.append('True')
        else:
            a.append('False')
    if len(set(a))>1:
        return True
    return False
print(circular(l,l1))