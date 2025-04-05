import functools,time, math
#1

arr = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x*y, arr))
#2

string = 'ExaMple'
upper = sum(map(lambda x: x.isupper(), string))
lower = sum(map(lambda x: x.islower(), string))
print(f"Upper: {upper}, lower: {lower}")
#3

string2 = input()
print(string2 == string2[::-1])
#4

def root(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)
rootOf = float(input())
ms = float(input())
print(f"Square root of {rootOf} after {ms} miliseconds is {root(rootOf, ms)}")
#5

tuple = (True, True, True, False)
print(all(tuple))