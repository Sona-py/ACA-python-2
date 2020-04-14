string = input("Please enter the word : ")
str1 = ""

for i in string:
    str1 = i + str1
if(string == str1):
   print("True")
else:
   print("False")