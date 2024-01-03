import re
def func(message):
    pattern = re.compile(r'[^A-Za-z0-9]')
    s = pattern.search(message)
    return not bool(s)

print(func("asdgdyug326fdyi72"))
print(func("s$$.adf23o78ro."))
