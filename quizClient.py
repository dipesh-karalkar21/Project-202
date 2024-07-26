import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.configure(bg="#252525")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        
        self.pls = Label(self.login,text = "Please login to continue",justify = CENTER,font = "Helvetica 14 bold",fg="white",bg="#252525")
        self.pls.place( relheight = 0.15,relx = 0.2,rely = 0.07)

        self.labelName = Label(self.login,text = "Name: ",font = "Helvetica 12",fg="white",bg="#252525")
        self.labelName.place(relheight = 0.2,relx = 0.1,rely = 0.2)

        self.entryName = Entry(self.login,font = "Helvetica 14",fg="white",bg="#252525")
        self.entryName.place(relwidth = 0.4,relheight = 0.12,relx = 0.35,rely = 0.25)
        self.entryName.focus()

        self.loginButton = Button(self.login,text="Login",font="Helvetica 14",command=lambda:self.goAhead(self.entryName.get()),fg="black",bg="#868686")
        self.loginButton.place(relx=0.4,rely=0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.name = name
        self.login.destroy()

        receive = Thread(target=self.receive)
        receive.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured!")
                client.close()
                break

g = GUI()

#def write():
#    while True:
#        message = input("")
#        client.send(message.encode('utf-8'))

#write_thread = Thread(target=write)
#write_thread.start()
