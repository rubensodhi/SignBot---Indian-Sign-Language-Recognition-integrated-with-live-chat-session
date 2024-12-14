import socket
import time
import threading
from threading import Thread
from tkinter import *
from multiprocessing import Process,freeze_support
def loop():
    file = open('out.txt', 'r')
    text.config(text=file.read())
    root.after(500, loop) # run every 500 milliseconds
    file.close()


def func():
    t = threading.Thread(target=recv)
    t.start()


def recv():
    listensocket = socket.socket()
    port = 3050
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()

    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage == "":
            time.sleep(5)
            lstbx.insert(0, "Client : " + sendermessage)


def sendmsg():
    s=0
    if s==0:
        f = open('out.txt', 'w')
        f.write("")
        f.close()
        s=socket.socket()
        hostname='CJ'
        port=4050
        msg = text.cget("text")
        print(msg)
        s.connect((hostname,port))
        lstbx.insert(0,"You : "+ msg)
        s.send(msg.encode())
    else:
        msg = text.cget("text")
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
 
 
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
def clearmsgbox():
    f = open("out.txt", "w")
    f.write("")
    f.close()

def resetChat():
    lstbx.delete(0,'end')

def chattMain():
    freeze_support()
    global root
    global text
    global lstbx
    text = "Hello"
    root=Tk()
    #root=Toplevel()
    root.geometry("400x600")
    root.config(bg="white")


    clearchatbox = PhotoImage(file='clear.png')
    clearbutton=Button(root,image=clearchatbox,command=clearmsgbox,borderwidth=0)
    clearbutton.place(x=350,y=550)


    startchatimage=PhotoImage(file='start.png')

    buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
    buttons.place(x=90,y=10)

    # message=StringVar()
    # messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=28)
    # messagebox.insert(0,text)
    text = Label(root, text='')
    text.place(x=10,y=550)

    sendmessageimg=PhotoImage(file='send.png')

    sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
    sendmessagebutton.place(x=300,y=550)

    lstbx=Listbox(root,height=20,width=42)
    lstbx.place(x=15,y=100)



    resetchat = PhotoImage(file='reset.png')
    resetbutton=Button(root,image=resetchat,command=resetChat,borderwidth=0)
    resetbutton.place(x=300,y=10)

    user_name = Label(root,text =" Number" ,width=10)

    loop()
    root.mainloop()
    #root.mainloop()
def MedChat():
    p = Thread(target=chattMain)
    p.start()
