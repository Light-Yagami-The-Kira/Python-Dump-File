class Dad:
    basketball = 1

class Son(Dad):
    dance = 1

    @staticmethod
    def isDance():
        print("I like to dance.")

class Grandson(Son):

    @staticmethod
    def isDance():
        print("I dont")

dave = Dad()
dav = Son()
da = Grandson()
dav.isDance()
da.isDance()
print(da.basketball)