import threading
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, sender):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        msg.send()


def send_html_mail(subject, html_content, recipient_list, sender):
    EmailThread(subject, html_content, recipient_list, sender).start()


def calculate_percentage(level, empty, full):
    # full = 3
    x = float(level) - float(full)
    y = float(empty) - float(full)
    x_div_y = x / y
    percentage = (1 - x_div_y) * 100
    pretty_percentage = round(percentage, 2)

    return pretty_percentage


def smell_quality(level):
    if level > 1.70:
        return "Bad"
    else:
        return "Good"
