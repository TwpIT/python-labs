mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))
