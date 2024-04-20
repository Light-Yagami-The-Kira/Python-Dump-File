import re
def func(message):
    # pattern = re.compile(r'^abbb')
    pattern = re.compile(r'^ab{3}')
    s = pattern.search(message)
    return bool(s)

print(func('a'))
print(func('abb'))
print(func('abb'))
print(func('abbb'))
print(func('abbbcsefd'))

