def all_positive(k,*args):
    return sum((abs(x) for x in args),abs(k))>sum(args,k)

def xor3(a,b,c):
    return bool((a and b and c) or (a and not(b) and not(c)) or (b and not(a) and not(c)) or (c and not(a) and not(b)))

def binary_sum(x:str,y:str):
    return int(x,2)+int(y,2)

def only_names(l):
    return list(filter(lambda x: x != "", l))

discriminant = lambda a, b, c : b**2-4*a*c

full_name=lambda x,y: x+' '+y


