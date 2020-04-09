def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac
if __name__ == "__main__":
    n=int(input("Enter the number"))
    print(factorial(n))