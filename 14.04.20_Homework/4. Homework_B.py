h=int((input("Enter the number:")))
def sumofd(h):
    if h==0:
        return 0
    return h%10+sumofd(h//10)
print(sumofd(h))