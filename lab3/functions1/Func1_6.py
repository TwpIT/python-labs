def reversed_string(string):
    string = string.split()
    newstring = ''
    for i in string[::-1]:
        newstring += i + ' '
    return newstring

print(reversed_string(input()))