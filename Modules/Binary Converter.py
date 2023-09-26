def binaryConverter(a):
    output=""
    if a == 0:
        output = "0"
    elif a == 1:
        output = "1"
    else:
        while True:
            r = int(a%2) #r is remainder which is a binary bit accord. to prime fact. method
            output += str(r)
            if r == a:
                break
            else:
                a = (a-r)/2   #a is dividend and a-r/2 is quotient by euclid division lemma
        
        output = output[::-1] #remainder digits are reversed accord. to prime fact method
    return output
