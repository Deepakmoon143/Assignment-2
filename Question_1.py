letter_to_ascii = {} 

for i in range(ord('a'), ord('z') + 1):
    letter_to_ascii[chr(i)] = i

print(letter_to_ascii)
