l=[[1,2],[1,2],[1,2,3]]
def repeat(l):
    try:
        return list(set(list(map(tuple,l))))
    except:
        return list(set(l))
print(repeat(l))
