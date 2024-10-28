import os

# print()
# print(os.getcwd())

# print()
files = os.listdir()
# print(type(files))
# print(files)

print()
print()

for file in files:
    os.rename(file, file[7:])
