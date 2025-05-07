import json
import tkinter as tk

class Lokaal:
    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    def naar_dict(self):
        return {
            "naam": self.naam,
            "richting": self.richting
        }


lokalen = [
    Lokaal("C1.13", "west"),
    Lokaal("C1.04", "west"),
    Lokaal("C1.06", "west")
]

lokalen_dict = [lokaal.naar_dict() for lokaal in lokalen]

with open("lokalen.json", "w") as f:
    json.dump(lokalen_dict, f, indent=4)