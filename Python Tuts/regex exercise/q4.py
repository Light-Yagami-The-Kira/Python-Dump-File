import re
def func(message):
    pattern = re.compile(r'^a(b+)')
    s = pattern.search(message)
    return bool(s)

print(func('ab'))
print(func('abc'))
print(func('abbc'))
print(func('aabbc'))