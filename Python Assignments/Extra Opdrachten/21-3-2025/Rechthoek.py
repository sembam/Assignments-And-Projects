import tkinter as tk

window = tk.Tk()
window.title("triangle")
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()
points = [300, 100, 100, 300, 500, 300]
canvas.create_polygon(points, fill="red", outline="black")
window.mainloop()