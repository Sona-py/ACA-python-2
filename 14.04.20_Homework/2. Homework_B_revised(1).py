a = [1,2,3,1,1]
newlist1 = [i for n, i in enumerate(a) if i not in a[:n]]
print(newlist1)