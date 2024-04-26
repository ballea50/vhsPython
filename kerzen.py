KERZEN = input("Anzahl Kerzen? ")
NAECHTESLOESCHEN = input("Anzahl bis zum nächsten Löschen? ")
#konvertieren
ANZAHLKERZEN = int(KERZEN)
MAXSCHRITTE = int(NAECHTESLOESCHEN)
#zunächst brennen alle Kerzen
brennendeKerzen = ANZAHLKERZEN
kerzenZustandsliste = [1] * ANZAHLKERZEN
print(kerzenZustandsliste)

#Startposition
z = 0
kerzenPosition = 0

#Solange noch mehr als 1 Kerze brennt
while brennendeKerzen > 1:
    if kerzenZustandsliste[kerzenPosition] == 1:
        z = z + 1
        if z == MAXSCHRITTE:
            #Lösche Kerze
            kerzenZustandsliste[kerzenPosition] = 0 
            brennendeKerzen = brennendeKerzen - 1
            print(kerzenZustandsliste)
            z = 0
    #Vorrücken auf nächste Position             
    kerzenPosition = kerzenPosition + 1
    if kerzenPosition == ANZAHLKERZEN:
       kerzenPosition = 0     
        
print("Fertig!")
print (f"Es brennt noch die Kerze an Position {kerzenZustandsliste.index(1)+1}")
