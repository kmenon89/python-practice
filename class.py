class chunju (object):
    def __init__(self,umma):
        kimma = umma
        self.umma = umma
        print("umma:", umma, " kimma:", kimma)

    def org(self):
        self.umma = "org umma"
        print("org umma:", self.umma)

    def org2(self):
        print("org2 umma:", self.umma)



c=chunju("chan")
c .org2()
c.org()
c.org2()