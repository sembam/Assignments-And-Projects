print("geef de lengte van zijde 1")
zijde1 = float(input("? "))
print("geef de lengte van zijde 2")
zijde2 = float(input("? "))

langezijde = round(((zijde1**2 + zijde2**2)**0.5), 1)

print(f"Korte zijde 1 = {zijde1}")
print(f"korte zijde 2 = {zijde2}")
print(f"lange zijde   = {langezijde}")