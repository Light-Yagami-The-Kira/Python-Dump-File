n = int(input("Enter value of n :: "))
space = " "
star = "*"
count = 1
for i in range(n,0,-1):
    print(f"{space*(i-1)}{star*(count)}{space*(i-1)}")
    count = count + 2
