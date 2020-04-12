a=int(input())
c=(bin(a)[2::])
total=0
for i in c:
    total+=int(i)
print(total)