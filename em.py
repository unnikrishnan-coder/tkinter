import tkinter as tk
from tkinter import *
import smtplib
from email.mime.text import MIMEText

 
root = tk.Tk()
root.title('Billing Software')
root.geometry('700x600')


def send():
    username = str(user_entry.get())
    password = str(password_entry.get())
    to_mail = str(to_entry.get())
    subject = str(subject_entry.get())
    content = str(content_entry.get('1.0', "end-1c"))
    
    message = MIMEText(content)
    message['SUBJECT'] = subject
    message['FROM'] = username
    message['TO'] = to_mail
    
    
    
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to_mail, message.as_string())
        result = tk.Label(root, text='DONE')
        result.pack()
        server.quit()



user = tk.Label(root, text='Username', padx=10, pady=10)
user.pack()
user_entry = tk.Entry(root,borderwidth=10)
user_entry.pack()
password = tk.Label(root, text="Password",padx=10, pady=10)
password.pack()
password_entry = tk.Entry(root,show='*', borderwidth=10)
password_entry.pack()
to = tk.Label(root, text="to",padx=10, pady=10)
to.pack()
to_entry = tk.Entry(root,borderwidth=10)
to_entry.pack()
subject = tk.Label(root, text='subject',padx=10, pady=10)
subject.pack()
subject_entry = tk.Entry(root,borderwidth=10)
subject_entry.pack()
content = tk.Label(root, text='content',padx=10, pady=10)
content.pack()
content_entry = tk.Text(root,borderwidth=10, height=10, width=20)
content_entry.pack()
send = tk.Button(root, text='Send',command=send,padx=10, pady=10)
send.pack()

root.mainloop()