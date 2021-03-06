def all_positive(k,*args):
    return sum((abs(x) for x in args),abs(k))>sum(args,k)

def xor3(a,b,c):
    return bool((a and b and c) or (a and not(b) and not(c)) or (b and not(a) and not(c)) or (c and not(a) and not(b)))

def binary_sum(x:str,y:str):
    return int(x,2)+int(y,2)

only_names=lambda x: x != ""

discriminant = lambda a, b, c : b**2-4*a*c

full_name=lambda x,y: x+' '+y


def mirror_string(a:str):
    n=list(a)
    b=[]
    s=''
    for i in n:
        if 65<=ord(i)<= 90:
            b.append(chr(90-(26-(90-ord(i))-1)))

        elif 97<=ord(i)<=122:
            b.append(chr(122-(26-(122-ord(i))-1)))

        else:
            b.append(i)

    return s.join(b)


def bit_concat(l):
    spl=[]
    jon=[]

    if 0<=len(l)<=4:
       l1=['{:08b}'.format(l[i]) for i in range(len(l))]
    lr=l1[::-1]

    for i in lr:
        spl.append([i[j:j + 2] for j in range(0, len(i),2)])

    for i in range(len(spl)):
        if spl[i][i]!='00':
            jon.append((spl[i][i]))
        elif spl[i][1]!='00':
            jon.append((spl[i][1]))
        elif spl[i][2]!='00':
            jon.append((spl[i][2]))
        else:
            jon.append((spl[i][3]))
    return int("".join(jon),2)
print(bit_concat([3,12]))

