try :
    f = open("README.txt", "r")
except Exception as e:
    print(e)
else:
    # THIS WILL RUN IF EXCEPT IS NOT RUNNING
    print("Else line.")
finally:
    print("Final Stuff")

print("IMportant stuff")
try :
    f = open("READMsadfadfasfdE.txt", "r")
except Exception as e:
    print(e)
else:
    # THIS WILL RUN IF EXCEPT IS NOT RUNNING
    print("Else line.")
finally:
    print("Final Stuff")

print("IMportant stuff")
