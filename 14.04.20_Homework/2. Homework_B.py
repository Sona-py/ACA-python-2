a = [[],[]]
b = []
[b.append(item) for item in a if item not in b]
print(b)