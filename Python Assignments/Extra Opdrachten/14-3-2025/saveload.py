import json
import tkinter as tk
from tkinter import messagebox


def save_entry():
    title = title_entry.get()
    author = author_entry.get()

    with open("01_names.json", "r") as json_file:
        data = json.load(json_file)

    y = {"title": title, "author": author}
    data["names"].append(y)

    write_json(data)
    
    messagebox.showinfo("Success", "Entry saved successfully!")

    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)


def load_entries():

    with open("01_names.json", "r") as f:
        content = json.load(f)
        output = json.dumps(content, separators=(",", ":"), indent=4)
        messagebox.showinfo("Stored Entries", content["names"])

def write_json(data, filename="01_names.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)



root = tk.Tk()
root.title("Song entry form")

# Voor styling chatgpt gebruikt

# Title Entry
tk.Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=10, pady=5)

# Author Entry
tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=5)
author_entry = tk.Entry(root, width=40)
author_entry.grid(row=1, column=1, padx=10, pady=5)

# Save Button
save_button = tk.Button(root, text="Save Entry", command=save_entry)
save_button.grid(row=2, column=0, padx=10, pady=10)

# Load Button
load_button = tk.Button(root, text="Load Entries", command=load_entries)
load_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()


