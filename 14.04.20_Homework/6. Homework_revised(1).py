a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
big = max(a, b)
small = min(a, b)
def divider(big,small):
    if big%small==0:
        return small
    return divider(small,big%small)
print(divider(big,small))

