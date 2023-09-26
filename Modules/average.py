import separator

I = input("Enter values :: ")

value_list = separator.separator(I , ",;")
s = 0
for i in range(0,len(value_list)):
    s = s + int(value_list[i])
    av = s/len(value_list)
print(av)