#Bestimmt ob eingegebenes Jahr ein Schaltjahr ist

import numpy

jahr = int(input())

schalter = 0

if jahr % 4 == 0:
   if jahr % 100 == 0:
      if jahr % 400 == 0: schalter = 1
   else:
      schalter = 1
if schalter == 0:
   print ("KEIN Schaltjahr !")
else:
   print ("Schaltjahr !")         

         

    
      


   
    