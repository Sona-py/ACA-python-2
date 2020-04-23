def last_digit(N):
    return int(((N*(N+1)*(2*N+1))/6)%10)

def is_polyndrome(word):
    return sum(map(lambda x: word.count(x) % 2, set(word))) <= 1

def quick_or(l):
    return bool(sum(l))

def expr_value(a):
    return "{:.2f}".format(eval(a))

def implication3(a,b,c):
    if a and b and not c:
        return False
    return True
