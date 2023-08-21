user_input1 = input("enter the starting ASCII values: ")
user_input2 = input("enter the ending ASCII values: ")
text = {}
for i in range(ord(user_input1), ord(user_input2)+1):
    text [chr(i)] = i
print(text)
