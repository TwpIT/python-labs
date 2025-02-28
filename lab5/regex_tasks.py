import re

#1
def match_a_b(s):
    return re.fullmatch(r'a[b]*', s)

print(match_a_b("abbb"))

#2
def match_a_bb(s):
    return re.fullmatch(r'a{1}b{2,3}', s)

print(match_a_bb("abb"))

#3
def find_lowercase_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

print(find_lowercase_underscore("abc_def ghi_jkl"))

#4
def find_upper_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

print(find_upper_lower("HelloWorld TestString"))

#5
def match_a_any_b(s):
    return re.fullmatch(r'a.*b', s)

print(match_a_any_b("a123b"))

#6
def replace_with_colon(s):
    return re.sub(r'[ .,]', ':', s)

print(replace_with_colon("Hello, world. How are you?"))

#7
def snake_to_camel(s):
    components = s.split('_')
    camel_case_str = components[0] + ''.join(word.title() for word in components[1:])
    return camel_case_str

print(snake_to_camel("hello_world"))

#8
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

print(split_at_uppercase("HelloWorldTest"))

#9
def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(insert_spaces("HelloWorldTest"))

#10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

print(camel_to_snake("HelloWorldTest"))