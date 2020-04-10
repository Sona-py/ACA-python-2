l = [1,2,3,1]
def repeat(l):
    s=sorted(l)
    h=len(s)-1
    for i in range(h):
        if s[i]==s[i+1]:
            s.remove(s[i])
            return(s)
        return(l)
print(repeat(l))





