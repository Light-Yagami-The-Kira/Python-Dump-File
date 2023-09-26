def check_int_float(I):
    if float(I) - int(I) == 0:
        cond = True
    else:
        cond = False
    return cond
if __name__ == "__main__":
    s = float(input("::: "))
    print(check_int_float(s))