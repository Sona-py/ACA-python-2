word=input("Enter the word:")
def symmetric(word):
    if len(word)==0 or len(word)==1:
        return True
    for i in range(len(word)//2):
        if word[i]==word[-i-1]:
            return True
        else:
            return False
print(symmetric(word))