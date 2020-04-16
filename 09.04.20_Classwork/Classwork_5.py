n=int(input())
def factorial(n):
    b=n
    i=1
    while i>0:
        if b%i==0:
            b//=i
        else:
            break
        i+=1
    if b==1:
        return n
    return factorial(n+1)
print(factorial(n))



