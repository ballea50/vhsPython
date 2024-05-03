import random

class Lotterie:
    def __init__(self, anz_ziehungen, max):
        self.max = max 
        self.anz_ziehungen = anz_ziehungen
       
    def ziehung(self):
        kugeln = [i for i in range(1,self.max + 1)]
        gz = random.sample(kugeln, self.anz_ziehungen)
        return sorted(gz)

class Lotto(Lotterie):
    def __init__(self):
        Lotterie.__init__(self,6,49)

lotto = Lotto()
print(lotto.ziehung())
