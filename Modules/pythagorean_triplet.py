def pyth_triplet(c):
    def check_int_float(I):
        if float(I) - int(I) == 0:
            cond = True
        else:
            cond = False
        return cond
    a = 1
    l=[]
    act_list=[]
    while a < c:
        b = (c**2 - a**2)**0.5
        if check_int_float(b) == True:
            item = str(a) + "," + str(int(b)) 
            l.append(item)

        a = a+1
    act_len = int((len(l)/2))
    for j in range(0,act_len):
        act_list.append(l[j])
    return act_list
if __name__ == "__main__":
    print(pyth_triplet(int(input("Enter value ::: "))))
