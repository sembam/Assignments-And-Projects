vakkenlijst = ["JavaScript", "Python", "HTML", "CSS", "LiveScript", "PHP", "EcmaScript"]

print(f"a) vakkenlijst = {vakkenlijst}")
print(f"b) {len(vakkenlijst)}")
print(f"c) {vakkenlijst[1]}")
vakkenlijst.sort()
print(f"d) {vakkenlijst}")
vakkenlijst.remove("LiveScript")
print(f"e) {vakkenlijst}")
vakkenlijst.remove("PHP")
print(f"f) {vakkenlijst}")
vakkenlijst.remove("EcmaScript")
vakkenlijst.insert(1, "ES6")
print(f"g) {vakkenlijst}")
vakkenlijst.remove("HTML")
vakkenlijst.remove("JavaScript")
print(f"h) {vakkenlijst}")
# functie voor alles omzetten in kleine letters
x = [item.lower() for item in vakkenlijst]
print(f"i) {x}")
