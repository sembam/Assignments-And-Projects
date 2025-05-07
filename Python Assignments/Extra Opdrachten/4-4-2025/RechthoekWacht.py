import tkinter as tk

window = tk.Tk()
window.title("Rechthoek")
canvas = tk.Canvas(window, width=1000, height=2000)
canvas.pack()
points = [300, 100, 100, 300]
canvas.create_rectangle(points, fill="red", outline="black")

def DrawSecond():
    points2 = [600, 400, 400, 600]
    canvas.create_rectangle(points2, fill="#FFB6C1", outline="black")


window.after(2000, DrawSecond)

window.mainloop()
