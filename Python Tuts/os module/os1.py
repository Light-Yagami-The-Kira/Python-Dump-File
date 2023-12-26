import os
# print("\n".join(dir(os)))
print(os.getcwd())
print(os.getcwdb())

os.chdir('C://Users//Krishanu//Desktop')
print(os.getcwd())

print("\n".join(os.listdir()))
print("============================================")
print("\n".join(os.listdir("C://")))

# os.mkdir('New Folder')
# os.rmdir('new folder')

# os.makedirs("Folder1/Folder2/Folder3/folder4")

# os.rename("old name", "new name")

print(os.environ.get('Path'))

print(os.path.join("C:/", "/Users"))

print(os.path.exists('C://'))
print(os.path.exists('C:/'))
print(os.path.exists('E:/'))

# print(os.path.isfile("filename"))
# print(os.path.isdir("dirname"))
# print(os.path.islink("linkame"))