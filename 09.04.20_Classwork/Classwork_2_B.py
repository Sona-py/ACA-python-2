l1=['abc','abd','abe']
def common(l1):
    t=list(map(set,l1))
    for i in range(len(t)+1):
        return len(t[i]&t[i+1])
print(common(l1))
