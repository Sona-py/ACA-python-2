def smax(l):
    if len(set(l))==1:
        return 0.5
    else:
        nl=set(l)
        nl.remove(max(nl))
        return max(nl)
if __name__ == "__main__":
    l=[int(elem) for elem in input().split()]
    print(smax(l))
