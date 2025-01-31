fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in fruits:
    if x == "banana":
        continue
    print(x)


for i in range(6):
    print("X")

for x in fruits:
    if x == "banana":
        break
    print(x)


for x in [0, 1, 2]:
  pass