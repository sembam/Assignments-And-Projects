import tkinter as tk



iface = tk.Tk()
label = tk.Label(iface, text="Hallo!")
label.pack()
button = tk.Button(iface, text="Klik om af te sluiten", command=iface.destroy)
button.pack()
iface.title("titel")

iface.mainloop()