user1 = input("enter the first alphabet from a-z")
user2 = input("enter the last alphabet from a-z")
text = {}
for i in range(ord(user1), ord(user2)+1):
    text [chr(i)] = i
print(text)
