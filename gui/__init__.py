import tkinter as tk
from tkinter.font import BOLD

import pywhatkit as what


def main():
    window = tk.Tk()
    window.geometry('600x600')
    window.resizable(False, False)

    tk.Label(background='#011638',
             font=('Verdana', 25, BOLD),
             text='WhatsappAutomation',
             foreground='#ffffff').place(x=87, y=20)

    window.configure(background='#011638')

    window.mainloop()
