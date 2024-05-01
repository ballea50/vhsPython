def fahrenheit_celsius(f):
    """ Rechnet zu einem gegebenen fahrenheitwert f
        den zugehörigen celsiuswert.

        Parameter: f fahrenheitwert numerisch
        Rückgabe:  c celsiuswert (auf 1 Stelle gerundet) 
    """    
    c = (f-32)*5/9
    return round(c,1)

def celsius_fahrenheit(c):
    """ Rechnet zu einem gegebenen celsiuswert c
        den zugehörigen fahrenheitwert.

        Parameter: f celsiuswert numerisch
        Rückgabe:  f fahrenheitwert (auf 1 Stelle gerundet) 
    """    
    f = c*9/5 + 32
    return round(f,1), c

celsius = fahrenheit_celsius(90)
print(celsius)
print(fahrenheit_celsius(20))

fahrenheit, celsius = celsius_fahrenheit(25)
print(f"Fahrenheit: {fahrenheit} entspricht Celsius {celsius}")



