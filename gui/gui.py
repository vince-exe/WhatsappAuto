import tkinter as tk
from tkinter.font import BOLD
import webbrowser


class Gui:
    def __init__(self, size, res_w, res_h, background):
        self.window = tk.Tk()
        self.window.geometry(size)
        self.window.resizable(res_w, res_h)
        self.window.configure(background=background)
        self.state = 'menu'

    def chat(self):
        self.state = 'chat'
        self.window.destroy()

    def mainloop(self):
        self.window.mainloop()

    @staticmethod
    def link():
        webbrowser.open_new_tab('https://github.com/vince-exe')


def gui():
    window = Gui('600x600', False, False, '#011638')

    tk.Label(background='#011638',
             font=('Verdana', 25, BOLD),
             text='WhatsappAutomation',
             foreground='#ffffff').place(x=87, y=20)

    tk.Button(background='#0c2d63',
              activebackground='#0c2d63',
              font=('Verdana', 30, BOLD),
              text='Chat',
              activeforeground='#ffffff',
              foreground='#ffffff',
              command=lambda: window.chat(),
              highlightbackground='#0c2d63',
              borderwidth=9,
              padx=50).place(x=190, y=220)

    tk.Button(background='#0c2d63',
              activebackground='#0c2d63',
              font=('Verdana', 30, BOLD),
              text='Exit',
              activeforeground='#ffffff',
              foreground='#ffffff',
              command=exit,
              highlightbackground='#0c2d63',
              borderwidth=9,
              padx=58).place(x=190, y=400)

    tk.Button(background='#0c2d63',
              activebackground='#0c2d63',
              foreground='#ffffff',
              activeforeground='#ffffff',
              font=('Verdana', 20, BOLD),
              text='GitHub',
              borderwidth=7,
              highlightbackground='#0c2d63',
              command=window.link).place(x=445, y=530)

    window.mainloop()

    if window.state == 'chat':
        chat_window = Gui('600x600', False, False, '#011638')

        chat_window.mainloop()
