l1=['aabc','aabd','aabe']
def common(l1):
    t=list(map(set,l1))
    com=set.intersection(*t)
    return len(com)
print(common(l1))

