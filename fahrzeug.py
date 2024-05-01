import datetime
class Fahrzeug:  
   def __init__(self,modell, baujahr):  
        self.modell = modell  
        self.baujahr = baujahr  
   def display(self):  
        print("Modell:", self.modell," Baujahr:",self.baujahr, 
              " Alter:", self.getage()) 
   
   def getage(self):
       today = datetime.date.today()
       age = today.year - self.baujahr 
       return age    
      
c1 = Fahrzeug("Toyota", 2016)  
c1.display()
