import tkinter.messagebox as tk_msg
import tkinter as tk

import pywhatkit.core.exceptions

from message import Message


def send_message(number, message, hours, minute, mode_, group_id):
    if check_error(mode_, message, number.get(), group_id, hours.get(), minute):
        message = Message(number.get(), message.get('1.0', tk.END), int(hours.get()), int(minute.get()), mode_, group_id)

        check_exceptions(message)


def set_label(string, var_string, label):
    if string == 'contact':
        var_string.set(string)
    else:
        var_string.set(string)

    label.configure(text='Mode: ' + var_string.get())


def check_error(mode, message, number, group_id, hours, minutes):
    if mode != 'contact' and mode != 'group':
        tk_msg.showerror(title='Mode Error', message='mode format should be ("contact" or "group" but is "empty"')
        return False

    elif mode == 'contact':
        if len(number) > 13 or len(number) < 13:
            tk_msg.showerror(title='Number Error', message='Number must be 13 characters!')
            return False

        if len(group_id):
            tk_msg.showerror(title='Contact Error', message='Group Id must be empty if you want to write to a contact!')
            return False

    else:
        sliced = group_id[26:]  # cut the first 26 characters
        if len(sliced) < 22 or len(sliced) > 22:
            tk_msg.showerror(title='Group Id Error',
                             message='Invalid group id')
            return False

    if not len(message.get('1.0', 'end-1c')):
        tk_msg.showerror(title='Message Error', message='Text box used for the message is empty!')
        return False

    elif not len(hours) or not len(minutes.get()):
        tk_msg.showerror(title='Hours Error', message='Hours or Minutes are empty!!')
        return False

    elif int(minutes.get()) > 60 or int(minutes.get()) < 0:
        tk_msg.showerror(title='Minutes Error', message='Minutes can not be greater then 60 or lesser than 0!')
        return False

    return True


def check_exceptions(message):
    try:
        message.send_message()
    except ValueError:
        tk_msg.showerror(title='Time Error', message='Invalid time format!')

    except pywhatkit.core.exceptions.CallTimeException:
        tk_msg.showerror(title='Time Error',
                         message='Enter a longer time, because whatsapp takes a few seconds to open')

    except pywhatkit.core.exceptions.InternetException:
        tk_msg.showerror(title='Internet Error', message='You must be connected to the internet to send messages')
