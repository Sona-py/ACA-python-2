def vowel(c):
    return c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U'

def reverse(str):
    i=0
    j=len(str)-1
    while i<j:
        if not vowel(str[i]):
            i+=1
            continue
        if not vowel(str[j]):
            j-=1
            continue
        str[i],str[j]=str[j],str[i]
        i+=1
        j-=1
    return str
if __name__ == "__main__":
    str = "america"
    print(*reverse(list(str)), sep = "")


