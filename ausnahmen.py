import sys

print(sys.maxsize)
print(2 ** 63)
n = 2 ** 500000
print(n)
try:
  #Open im 'append modus'
  f = open("demofile.txt","a")
  try:
    f.write("Programmieren macht Spaß!")
  except:
    print("Fehler beim Schreiben")
  finally:
    f.close()
except:
  print("Fehler beim Öffnen") 