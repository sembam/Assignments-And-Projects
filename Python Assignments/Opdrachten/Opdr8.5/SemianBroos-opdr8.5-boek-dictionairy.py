import pprint

fav_boek = {
    "titel" : "Guns, germs and steel",
    "subtitel" : "The fates of human societies",
    "jaar" : 2007,
    "uitgever" : "Ww norton & Co"

}
fav_boek.update({"jaar" : 1997})
print(f"a) {fav_boek}")
fav_boek.update({"ISBN" : "0-393-03891-2"})
print(f"b {fav_boek}")
fav_boek.pop("subtitel")
print(f"c) {fav_boek}")
print(f"d) {fav_boek['uitgever']}")
print("e) ")
for x, y in fav_boek.items():
    print(f" {x, y}")
