
temp = float(input("Geef de temperatuur in graden celcius.\n"))

Celcius = round((temp), 2)
Fahrenheit = round(((temp * 9 / 5) + 32.0), 2)
Kelvin = round((temp + 273.15), 2)

print(f"Celcius    = {Celcius} oC")
print(f"Fahrenheit = {Fahrenheit} oF")
print(f"Kelvin     = {Kelvin} oK")
