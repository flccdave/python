import os

print()
print(os.getcwd())

print()
files = os.listdir()
print(type(files))
print(files)

print()
print()

for file in files:

    if file != "__pycache_":
        # os.rename(file, file[7:])
        temp_file = open(file, "a")
        temp_file.write('Dave was here')
