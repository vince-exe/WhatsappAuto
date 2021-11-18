import tkinter as tk
import webbrowser

from tkinter.font import BOLD
from message import Message


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


def send_message(number, message, hours, minute, mode_, group_id):
    message = Message(number, message, hours, minute, mode_, group_id)
    message.send_message()


def set_label(string, var_string, label):
    if string == 'contact':
        var_string.set(string)
    else:
        var_string.set(string)

    label.configure(text='Mode: ' + var_string.get())


def main_gui():
    window = Gui('600x600', False, False, '#011638')
    mode = tk.StringVar()
    mode.set('')

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
              command=window.chat,
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
        chat_window = Gui('1360x700', False, False, '#011638')

        tk.Label(font=('Verdana', 25, BOLD),
                 foreground='#ffffff',
                 background='#011638',
                 text='Chat with your friends!!').place(x=450, y=30)

        tk.Button(background='#0c2d63',
                  activebackground='#0c2d63',
                  foreground='#ffffff',
                  activeforeground='#ffffff',
                  font=('Verdana', 20, BOLD),
                  text='Contact',
                  command=lambda: set_label('contact', mode, mode_label),
                  borderwidth=7,
                  highlightbackground='#0c2d63').place(x=300, y=150)

        tk.Button(background='#0c2d63',
                  activebackground='#0c2d63',
                  foreground='#ffffff',
                  activeforeground='#ffffff',
                  font=('Verdana', 20, BOLD),
                  text='Group',
                  command=lambda: set_label('group', mode, mode_label),
                  borderwidth=8,
                  width=7,
                  highlightbackground='#0c2d63').place(x=830, y=150)

        message = tk.Text(
                width=50,
                font=('Verdana', 15),
                height=15,
                background='#c4c5cf',
                selectbackground='#c4c5cf')
        message.place(x=330, y=260)

        tk.Label(font=('Verdana', 20, BOLD),
                 foreground='#ffffff',
                 background='#011638',
                 text='Number').place(x=1178, y=530)

        number = tk.Entry(
                 bg='#c4c5cf',
                 font=('Verdana', 15),
                 selectbackground='#c4c5cf',
                 width=14)
        number.place(x=1150, y=575)

        tk.Label(font=('Verdana', 20, BOLD),
                 foreground='#ffffff',
                 background='#011638',
                 text='Group Id').place(x=1175, y=420)

        group_id = tk.Entry(
                 bg='#c4c5cf',
                 font=('Verdana', 15),
                 selectbackground='#c4c5cf',
                 width=14)
        group_id.place(x=1150, y=460)

        tk.Button(background='#0c2d63',
                  activebackground='#0c2d63',
                  foreground='#ffffff',
                  activeforeground='#ffffff',
                  font=('Verdana', 20, BOLD),
                  text='Send',
                  borderwidth=8,
                  command=lambda: send_message(number.get(), message.get('1.0', tk.END), int(hours.get()), int(minutes.get()), mode.get(), group_id.get()),
                  width=5,
                  highlightbackground='#0c2d63').place(x=30, y=630)

        tk.Label(font=('Verdana', 20, BOLD),
                 foreground='#ffffff',
                 background='#011638',
                 text='Hours').place(x=1196, y=300)

        hours = tk.Entry(
            bg='#c4c5cf',
            font=('Verdana', 15),
            selectbackground='#c4c5cf',
            width=14)
        hours.place(x=1150, y=340)

        tk.Label(font=('Verdana', 20, BOLD),
                 foreground='#ffffff',
                 background='#011638',
                 text='Minutes').place(x=1180, y=200)

        minutes = tk.Entry(
            bg='#c4c5cf',
            font=('Verdana', 15),
            selectbackground='#c4c5cf',
            width=14)
        minutes.place(x=1150, y=245)

        mode_label = tk.Label(font=('Verdana', 20, BOLD),
                              foreground='#ffffff',
                              background='#011638',
                              text='Mode: ')
        mode_label.place(x=20, y=30)

        chat_window.mainloop()
