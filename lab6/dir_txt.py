import os, string
#1

path = os.getcwd()
print(f"Files: {[f for f in os.listdir(path) if os.path.isfile(f)]}, directories: {[d for d in os.listdir(path) if os.path.isdir(d)]} all elements are: {os.listdir(path)}")
#2

path = os.getcwd()
print(f"Path accessibility: Existance: {os.access(path, mode=os.X_OK)}, Reading: {os.access(path, mode=os.R_OK)}, Writing: {os.access(path, mode=os.W_OK)}, Executability: {os.access(path, mode=os.X_OK)}")
#3

path = os.getcwd()
def checkUp(path):
    if os.access(path, mode=os.X_OK):
        return os.listdir(path)
    else:
        return False
print(checkUp(path))
#4

with open('lab6\example_f.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)
#5

list = list(input().split())
with open('lab6\example_f.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')
#6

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w'):
        pass
#7

with open('lab6\example_f.txt', 'r') as r:
    with open('copy_to.txt', 'w') as w:
        for line in r:
            w.write(line)
#8

if os.path.exists('example2.txt'):
    os.remove('lab6\example_f.txt')