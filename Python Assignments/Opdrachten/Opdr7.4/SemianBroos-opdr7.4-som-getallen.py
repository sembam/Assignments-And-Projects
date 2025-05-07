
start = 250
end = 500
cumulative_sum = 0
count = 0

for getal in range(start, end + 1):
    cumulative_sum += getal
    kwadraat = getal ** 2
    count += 1  
    print(f"Getal {getal}   Som {cumulative_sum}   Kwadraat {kwadraat}")
average = cumulative_sum / count

print(f"Het gemiddelde is van alle getal is {average}")

#deze opdracht was te moeilijk dus ik heb wat ai gebruikt