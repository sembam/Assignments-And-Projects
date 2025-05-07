import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sprite Animatie")


        self.spritesheet_run = Image.open("Mushroom-Run.png")
        self.spritesheet_idle = Image.open("Mushroom-Idle.png")

        self.num_sprites = 7
        self.sprite_width = 80
        self.sprite_height = 64

        self.frames_run = [
            ImageTk.PhotoImage(
                self.spritesheet_run.crop(
                    (i * self.sprite_width, 0, (i + 1) * self.sprite_width, self.sprite_height)).resize((64, 96))
            ) for i in range(self.num_sprites)
        ]

        self.frames_idle = [
            ImageTk.PhotoImage(
                self.spritesheet_idle.crop(
                    (i * self.sprite_width, 0, (i + 1) * self.sprite_width, self.sprite_height)).resize((64, 96))
            ) for i in range(self.num_sprites)
        ]


        self.current_animation = self.frames_run
        self.current_sprite = 0

        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.pack()
        self.sprite_obj = self.canvas.create_image(100, 150, image=self.current_animation[self.current_sprite])

        self.bind("<space>", self.switch_animation)
        self.animate()

    def animate(self):
        self.current_sprite = (self.current_sprite + 1) % self.num_sprites
        self.canvas.itemconfig(self.sprite_obj, image=self.current_animation[self.current_sprite])
        self.after(100, self.animate)

    def switch_animation(self, event):
        if self.current_animation == self.frames_run:
            self.current_animation = self.frames_idle
        else:
            self.current_animation = self.frames_run

        self.current_sprite = 0


app = App()
app.mainloop()
