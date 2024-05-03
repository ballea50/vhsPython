import datetime
#Basis- oder Elternklasse "Fahrzeug"
class Fahrzeug: 
    
   def __init__(self, hersteller, baujahr):  #Konstruktor
        self.hersteller = hersteller  
        self.baujahr = baujahr  
   
   def getAge(self):                         #Methode: getAge()   
       today = datetime.date.today()
       age = today.year - self.baujahr 
       return age  
   
   def display(self):  
        print("hersteller:", self.hersteller," Baujahr:",self.baujahr, 
              " Alter:", self.getAge())   
 

#Unterklasse oder subclass von Fahrzeug
class Fahrrad(Fahrzeug):
    #Übernommene Attribute und Methoden der abgeleiteten Klasse
    #werden in der der Subklasse nicht aufgeführt.
    #Ergänzende Attribute und Methoden werden wie üblich deklariert. 
    def __init__(self, hersteller, baujahr, typ):
        self.typ = typ   #neues Attribut
        Fahrzeug.__init__(self, hersteller, baujahr)
     
        
c1 = Fahrzeug("Toyota", 2016)  
c1.display()

f1 = Fahrrad("Kepler", 2022, "Pedelec")
f1.display()
print(f1.typ)
print(isinstance(f1,Fahrrad))