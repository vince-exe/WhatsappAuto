import tkinter as tk
import webbrowser


class Gui:
    def __init__(self, size, res_w, res_h, background):
        self.window = tk.Tk()
        self.window.geometry(size)
        self.window.resizable(res_w, res_h)
        self.window.configure(background=background)

    def chat(self):
        self.window.destroy()

    def mainloop(self):
        self.window.mainloop()

    @staticmethod
    def link():
        webbrowser.open_new_tab('https://github.com/vince-exe')
