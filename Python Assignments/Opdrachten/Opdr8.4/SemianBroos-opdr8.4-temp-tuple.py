
# variabelen
temp = (22.7, 30.8, 26.8, 19.3, 16.7, 38.9, 32.5, 27.5, 24.5)
result = 1
middel = temp[2:7]

# loop voor de vermenivuldiging
for value in temp:
    result *= value


# uitvoer
print(f"tuple: {temp}")
print(f"a) Min: {temp[5]}")
print(f"b) Max: {temp[4]}")
print(f"c) Aantal: {len(temp)}")
print(f"d) Vermenigvuldiging {result}")
print(f"e) middelste waarden {middel}")

