dict = {'a':45,'A':5,'B':5}

print(

    {k.lower():dict.get(k.lower(),10000)+dict.get(k.upper(),1000) for k in dict.keys()}
    
)