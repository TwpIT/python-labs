def unique_elements(list):
    return [i for i in list if list.count(i) == 1]
print(*unique_elements(input().split()))
lis = [1, 2 ,1, 3, 4]
print(*unique_elements(lis))