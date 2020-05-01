def compare_lists(a, b):
    if len(a)==len(b):
        if sum(a)==sum(b):
            return len(set(a + b)) == len(set(b))
    return False

def sort_list(l,order='ascending'):
    if all(isinstance(x, int) for x in l) and order=='ascending':
            if len(l)>1:
                mid = len(l)//2
                lefthalf = l[:mid]
                righthalf = l[mid:]

                sort_list(lefthalf)
                sort_list(righthalf)

                i=0
                j=0
                k=0
                while i < len(lefthalf) and j < len(righthalf):
                    if lefthalf[i] <= righthalf[j]:
                        l[k]=lefthalf[i]
                        i=i+1
                    else:
                        l[k]=righthalf[j]
                        j=j+1
                    k=k+1

                while i < len(lefthalf):
                    l[k]=lefthalf[i]
                    i=i+1
                    k=k+1

                while j < len(righthalf):
                    l[k]=righthalf[j]
                    j=j+1
                    k=k+1
            return l
    elif all(isinstance(x, int) for x in l) and order=='descending':
        return sort_list(l,'ascending')[::-1]

    
def all_sums(a):
    pairs=[]
    n=list(range(1,a))
    for i in n:
        j=a-i
        if j in n:
            pairs.append((i,j))
    pairs1 = [i for n, i in enumerate(pairs) if i[::-1] not in pairs[:n]]
    return pairs1


from collections import defaultdict
def duplicate_characters(s):
    d = defaultdict(int)
    dub=set()
    for k in s:
        d[k] = d[k]+1
    for k in d:
        if k!=' ' and d[k]>1:
            dub.add(k)
    return dub


def bisect_position(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def heapq(n, i):
   l=n+[i]
   for k in range(len(l)):
       node1=int(2*k+1)
       node2=int(2*k+2)
       parent=int(node2/2-1)
       try:
           if l[node1]>=l[parent] and l[node2]>=l[parent]:
               continue
           elif l[node1]<l[parent]:
               l[node1],l[parent]=l[parent],l[node1]
           elif l[node2] < l[parent]:
               l[node2], l[parent] = l[parent], l[node2]

       except IndexError as error:
           return l
