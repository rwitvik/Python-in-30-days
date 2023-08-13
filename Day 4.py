#1

str1 ="hello"
str2 ="world"
print(str1 +" "+ str2)




#2

str1= input("enter your name")
str2 = input("enter your greeting")
print(str1+ " "+str2)


#3

word= "chandu"
print(word * 5)


#4

senetence = "just chill"
print(len(senetence))


#5

str1= input("enter a sentence")
length=len(str1)
if length > 0:
    last_char = str1[-1]
else:
    print("empty string")
print(length)
print("last character: ", last_char)


#6
pattern ="*"
row=5
for i in range (1, row+1) :
    for j in range(i):
        print("*",end=" ")
    print()