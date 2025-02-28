#1
print("1:")
def make_squares(value):
    for i in range(value + 1):
        yield i ** 2

for square in make_squares(5):
    print(square)

#2
print("2:")
def even_numbers(n):
    val = 0
    while val!=n:
        if val%2==0:
            yield str(val)
        val+=1

n = int(input())
print(",".join(even_numbers(n)))

#3
print("3:")
def divide_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divide_3_4(20):
    print(num)

#4
print("4:")
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for num in squares(3, 7):
    print(num)

#5
print("5:")
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(10):
    print(num)
