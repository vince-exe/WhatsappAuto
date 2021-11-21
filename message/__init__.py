import pywhatkit


class Message:
    def __init__(self, number, message, hours, minute, mode_, group_id):
        self.number = number
        self.message = message
        self.hours = hours
        self.minute = minute
        self.mode = mode_
        self.group_id = group_id

    def send_message(self):
        if self.mode == 'contact':
            pywhatkit.sendwhatmsg(self.number, self.message, self.hours, self.minute)
        else:
            pywhatkit.sendwhatmsg_to_group(self.group_id, self.message, self.hours, self.minute)
