text_file = open("text.txt", "a")
# print(text_file)

print('Writable? ', text_file.writable())
print('Readable? ', text_file.readable())
text_file.write('ABCD\n')

# temp = text_file.readlines()
# print(temp)

# temp = text_file.readlines()
# print(temp)