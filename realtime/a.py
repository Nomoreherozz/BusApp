class a:
    def __init__(self, q=0) -> None:
        self.q = q+1

    def x4(self):
        return 4
    
    def x8(self):
        k = self.x4()
        return k*5
    

    def check(self):
        self.q += 999
        return self.q
    

z = a(7)
print(z.check())