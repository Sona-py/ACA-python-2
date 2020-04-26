def compare_lists(a,b):
    return len(set(a))==len(set(b))

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
