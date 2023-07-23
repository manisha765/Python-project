from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import main
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9101",
    database="python_database",
    port=3306,
    auth_plugin='mysql_native_password'
)


class Login():
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry("1500x1000+0+0")
        self.bg_image = ImageTk.PhotoImage(file="../Music Player/pexels-pixabay-531880.jpg")
        bg = Label(self.window, image=self.bg_image)
        bg.place(x=0, y=0, relheight=1, relwidth=1)

        global username  # our variables
        global password  # we use global for the other function to use it

        username = StringVar()  # we indicate what type of variables we declared
        password = StringVar()  # which is string type

        frame = Frame(self.window, bg="#c7dee5")
        frame.place(x=490, y=100, width=300, height=450)
        frame1 = Frame(self.window, bg="white")
        frame1.place(x=510, y=260, width=260, height=150)

        user_image = Image.open("../Music Player/image_1.jpg")
        user_image = user_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.user_image = ImageTk.PhotoImage(user_image)

        img_lbl = Label(image=self.user_image, bg="#c7dee5", borderwidth=0)
        img_lbl.place(x=598, y=110, width=100, height=100)

        get_label = Label(frame, text="Get Started", font=('Stencil', 20, 'bold'), fg="#1d4c45", bg='#c7dee5')
        get_label.place(x=70, y=110)

        # username label
        user_label = Label(frame1, text="Username", font=('Bahnschrift SemiBold Condensed', 14, 'bold'), fg='#1d4c45',
                           bg='white')
        user_label.place(x=10, y=1)
        pass_label = Label(frame1, text="Password", font=('Bahnschrift SemiBold Condensed', 14, 'bold'), fg='#1d4c45',
                           bg='white')
        pass_label.place(x=10, y=64)

        self.user_entry = ttk.Entry(frame1, font=('Franklin Gothic Book', 12, 'normal'), textvariable=username)
        self.user_entry.place(x=10, y=25, width=220)
        self.pass_entry = ttk.Entry(frame1, font=('Franklin Gothic BookL', 12, 'normal'), textvariable=password)
        self.pass_entry.place(x=10, y=90, width=220)

        login_button = Button(frame, text='Login', font=('Stencil', 15, 'bold'), bd=3, relief=RIDGE, fg='white',
                              bg='#1d4c45', activeforeground='#1d4c45', activebackground='#c7dee5',
                              command=log)
        login_button.place(x=90, y=320, width=120, height=35)


def log():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
        username.get(), password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():
        root = Tk()
        obj = main.LibraryManagementSystem(root)
        root.mainloop()

    else:
        print("Invalid Credentials")


if __name__ == '__main__':
    window = Tk()
    app = Login(window)
    window.mainloop()
