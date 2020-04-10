def vowel(c):
    return c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U'

def reverse(string):
    i=0
    j=len(str)-1
    while i<j:
        if not vowel(string[i]):
            i+=1
            continue
        if not vowel(string[j]):
            j-=1
            continue
        string[i],string[j]=string[j],string[i]
        i+=1
        j-=1
    return string
if __name__ == "__main__":
    string = "america"
    print(*reverse(list(str)), sep = "")


