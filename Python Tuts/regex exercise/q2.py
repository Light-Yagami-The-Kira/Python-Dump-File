import re
def func(message):
    # pattern = re.compile(r'^a(b*)$')
    pattern = re.compile(r'^(a(b+))$')
    s = pattern.search(message)
    return bool(s)

print(func(""))
print(func("a"))
print(func("aab"))
print(func("abb"))
print(func("abbbb"))
print(func("abc"))
print(func("ac"))
print(func("bbbba"))
print(func("bbbbaa"))