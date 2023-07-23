from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LibraryManagementSystem")
        self.root.geometry("1550x800+0+0")

        # Variable
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.mobile_var = StringVar()
        self.bookId_var = StringVar()
        self.bookTitle_var = StringVar()
        self.author_var = StringVar()
        self.dateBorrowed_var = StringVar()
        self.dateDue_var = StringVar()
        self.dateOverDue = StringVar()
        self.dateOnBook_var = StringVar()
        self.lateFine_var = StringVar()
        self.finalPrice_var = StringVar()

        title_label = Label(self.root, text="Library Management System", bg='#4d382f', fg="#aba3a0", bd=10,
                            relief=RIDGE,
                            font=("Stencil", 30, 'bold'), pady=6, padx=2)
        title_label.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=10, relief=RIDGE, padx=10, pady=10, bg="#4d382f")
        frame.place(x=0, y=80, height=380, width=1280)
        # ________________________________Left Data Frame___________________________________________
        DataFrameLeft = LabelFrame(frame, text="Library Membership information", bg="#aba3a0", fg="#4d382f", bd=10,
                                   relief=RIDGE, font=("Lucida Calligraphy", 16, "bold"))
        DataFrameLeft.place(x=0, y=0, width=860, height=345)

        # ---------------------------------Label_____________________________________________________
        member_label = Label(DataFrameLeft, text="Member Type",
                             font=("times new roman", 15, "bold"), pady=3, padx=2,
                             bg="#aba3a0", fg="#4d382f")
        member_label.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.member_var,
                                 width=23, state="readonly")
        comMember["value"] = ("Admin staff", "Student", "lecturer")
        comMember.grid(row=0, column=1)

        PRN_label = Label(DataFrameLeft, text="PRN NO", font=("times new roman", 15, "bold"), pady=3, padx=2,
                          bg="#aba3a0", fg="#4d382f")
        PRN_label.grid(row=1, column=0, sticky=W)

        txtPRN = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.prn_var, width=25)
        txtPRN.grid(row=1, column=1)
        lblTitle = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text=" ID NO", font=("times new roman", 15, "bold"),
                         padx=2,
                         pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.id_var, width=24)
        txtTitle.grid(row=2, column=1)

        lblFirstname = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="First Name",
                             font=("times new roman", 15, "bold"),
                             padx=2,
                             pady=6)
        lblFirstname.grid(row=3, column=0, sticky=W)
        txtFirstname = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.firstname_var,
                             width=24)
        txtFirstname.grid(row=3, column=1)

        lblLastname = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Last Name",
                            font=("times new roman", 15, "bold"), padx=2,
                            pady=6)
        lblLastname.grid(row=4, column=0, sticky=W)
        txtLastname = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.lastname_var,
                            width=24)
        txtLastname.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Address",
                            font=("times new roman", 15, "bold"), padx=2,
                            pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.address1_var,
                            width=24)
        txtAddress1.grid(row=5, column=1)

        lblMobileNo = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="MobileNo",
                            font=("times new roman", 15, "bold"), padx=2,
                            pady=5)
        lblMobileNo.grid(row=6, column=0, sticky=W)
        txtMobileNo = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.mobile_var, width=24)
        txtMobileNo.grid(row=6, column=1)

        lbldateonbook = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Date On Book",
                              font=("times new roman", 15, "bold"),
                              padx=2,
                              pady=3)
        lbldateonbook.grid(row=7, column=0, sticky=W)
        txtdateonbook = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.dateOnBook_var,
                              width=24)
        txtdateonbook.grid(row=7, column=1)

        lblBookID = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Book ID",
                          font=("times new roman", 15, "bold"), padx=2,
                          pady=6)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.bookId_var, width=24)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Book Title",
                             font=("times new roman", 15, "bold"),
                             padx=2,
                             pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.bookTitle_var,
                             width=24)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Author",
                          font=("times new roman", 15, "bold"), padx=2,
                          pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.author_var, width=24)
        txtAuthor.grid(row=2, column=3)

        lblBorroweddate = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Borrowed Date",
                                font=("times new roman", 15, "bold"),
                                padx=2, pady=6)
        lblBorroweddate.grid(row=3, column=2, sticky=W)

        txtBorroweddate = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.dateBorrowed_var,
                                width=24)
        txtBorroweddate.grid(row=3, column=3)

        lblDatedue = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Date Due",
                           font=("times new roman", 15, "bold"), padx=2,
                           pady=6)
        lblDatedue.grid(row=4, column=2, sticky=W)

        txtDatedue = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.dateDue_var, width=24)
        txtDatedue.grid(row=4, column=3)

        lblLastreturnfine = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="LateReturnFine",
                                  font=("times new roman", 15, "bold"),
                                  padx=2, pady=6)
        lblLastreturnfine.grid(row=5, column=2, sticky=W)
        txtLastreturnfine = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.lateFine_var,
                                  width=24)
        txtLastreturnfine.grid(row=5, column=3)

        lblDateoverdue = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="DateOverDue",
                               font=("times new roman", 15, "bold"),
                               padx=2, pady=3)
        lblDateoverdue.grid(row=6, column=2, sticky=W)
        txtDateoverdue = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.dateOverDue,
                               width=24)
        txtDateoverdue.grid(row=6, column=3)

        lblActualprice = Label(DataFrameLeft, bg="#aba3a0", fg="#4d382f", text="Actual Price",
                               font=("times new roman", 15, "bold"),
                               padx=2, pady=3)
        lblActualprice.grid(row=7, column=2, sticky=W)
        txtActualprice = Entry(DataFrameLeft, font=("Bahnschrift SemiBold SemiConden", 12, "normal"), textvariable=self.finalPrice_var,
                               width=24)
        txtActualprice.grid(row=7, column=3)

        # _______________________________Right Data Frame__________________________________________
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="#aba3a0", fg="#4d382f", bd=10,
                                    relief=RIDGE, font=("Lucida Calligraphy", 16, "bold"))
        DataFrameRight.place(x=870, y=0, width=370, height=345)

        self.textbox = Text(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=15, padx=2, pady=6)
        self.textbox.grid(row=0, column=2)
        listScroll_bar = Scrollbar(DataFrameRight)
        listScroll_bar.grid(row=0, column=1, sticky='ns')

        listBook = ["Python Crash Course", "Head-First Python, 2nd edition",
                    "Think Python",
                    "Learn Python 3 the Hard Way",
                    "Real Python Course"]

        def selectedBook(event):
            widget = event.widget
            selection = widget.curselection()
            value = str(listBox.get(selection))
            x = value
            if x == "Python Crash Course":
                self.bookId_var.set("BKID1")
                self.bookTitle_var.set("Python Crash Course")
                self.author_var.set("Eric Matthes")
                d1 = str(datetime.datetime.today())
                d2 = str(datetime.timedelta(days=15))
                d3 = d1 + d2
                self.dateBorrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.dateOnBook_var.set("2019-05-03")
                self.lateFine_var.set("Rs.50")
                self.dateOverDue.set("No")
                self.finalPrice_var.set("Rs 780")

            elif x == "Head-First Python, 2nd edition":
                self.bookId_var.set("BKID2")
                self.bookTitle_var.set("Head-First Python")
                self.author_var.set("Paul Barry")
                d1 = str(datetime.datetime.today())
                d2 = str(datetime.timedelta(days=15))
                d3 = d1 + d2
                self.dateBorrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.dateOnBook_var.set("2020-01-06")
                self.lateFine_var.set("Rs.50")
                self.dateOverDue.set("No")
                self.finalPrice_var.set("Rs 800")

            elif x == "Think Python":
                self.bookId_var.set("BKID3")
                self.bookTitle_var.set("Think Python")
                self.author_var.set("Allen Downey")
                d1 = str(datetime.datetime.today())
                d2 = str(datetime.timedelta(days=15))
                d3 = d1 + d2
                self.dateBorrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.dateOnBook_var.set("2016-07-08")
                self.lateFine_var.set("Rs.40")
                self.dateOverDue.set("No")
                self.finalPrice_var.set("Rs 700")

            elif x == "Learn Python 3 the Hard Way":
                self.bookId_var.set("BKID4")
                self.bookTitle_var.set("Learn Python 3 the Hard Wayn")
                self.author_var.set("Zed Shaw")
                d1 = str(datetime.datetime.today())
                d2 = str(datetime.timedelta(days=15))
                d3 = d1 + d2
                self.dateBorrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.lateFine_var.set("Rs.40")
                self.dateOnBook_var.set("2020-09-16")
                self.dateOverDue.set("No")
                self.finalPrice_var.set("Rs 700")

            elif x == "Real Python Course":
                self.bookId_var.set("BKID5")
                self.bookTitle_var.set("Real Python Course")
                self.author_var.set("Dan Bader")
                d1 = str(datetime.datetime.today())
                d2 = str(datetime.timedelta(days=15))
                d3 = d1 + d2
                self.dateBorrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.lateFine_var.set("Rs.40")
                self.dateOnBook_var.set("2014-11-06")
                self.dateOverDue.set("No")
                self.finalPrice_var.set("Rs 460")

        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=15)
        listBox.bind("<<ListboxSelect>>", selectedBook)
        listBox.grid(row=0, column=0, padx=4)
        listScroll_bar.config(command=listBox.yview)
        for item in listBook:
            listBox.insert(END, item)
        # _____________________________________Button Frame____________________________________
        button_frame = Frame(self.root, bd=10, relief=RIDGE, padx=10, pady=10, bg="#4d382f")
        button_frame.place(x=0, y=453, height=70, width=1280)

        add_button = Button(button_frame, text="Add Data", font=("times new roman", 12, "bold"), bg="#aba3a0",
                            fg="#4d382f", width=20,
                            command=self.add_data, activebackground='#4d382f', activeforeground="#aba3a0")
        add_button.grid(row=0, column=0)

        show_button = Button(button_frame, command=self.show_data, text="Show Data", bg="#aba3a0", fg="#4d382f",
                             font=("times new roman", 12, "bold"), width=20, activebackground='#4d382f',
                             activeforeground="#aba3a0")
        show_button.grid(row=0, column=1)

        update_button = Button(button_frame, command=self.update, text="Update", bg="#aba3a0", fg="#4d382f",
                               font=("times new roman", 12, "bold"), width=20, activebackground='#4d382f',
                               activeforeground="#aba3a0")
        update_button.grid(row=0, column=2)

        delete_button = Button(button_frame, command=self.delete, text="Delete", bg="#aba3a0", fg="#4d382f",
                               font=("times new roman", 12, "bold"), width=20, activebackground='#4d382f',
                               activeforeground="#aba3a0")
        delete_button.grid(row=0, column=3)

        reset_button = Button(button_frame, command=self.reset, text="Reset", bg="#aba3a0", fg="#4d382f",
                              font=("times new roman", 12, "bold"),
                              width=20, activebackground='#4d382f', activeforeground="#aba3a0")
        reset_button.grid(row=0, column=4)

        exit_button = Button(button_frame, command=self.iexit, text="Exit", bg="#aba3a0", fg="#4d382f",
                             font=("times new roman", 12, "bold"), activebackground='#4d382f',
                             activeforeground="#aba3a0",
                             width=20)
        exit_button.grid(row=0, column=5)

        # _________________________________Table data______________________________________
        detail_frame = Frame(self.root, bd=10, relief=RIDGE, padx=10, pady=10, bg="#4d382f")
        detail_frame.place(x=0, y=455 + 70, height=130, width=1280)

        Table_frame = LabelFrame(detail_frame, bd=6, relief=RIDGE, bg="#aba3a0",font=("Bahnschrift SemiBold SemiConden", 10, "bold"))
        Table_frame.place(x=0, y=1, width=1240, height=95)

        x_scroll = Scrollbar(Table_frame, orient=HORIZONTAL)

        y_scroll = Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, columns=('membertype', 'prnno', 'title', 'firstname', 'lastname'
                                                                , 'address', 'mobileid', 'bookid',
                                                                'booktitle', 'author', 'dateborrowed', 'datedue',
                                                                'days',
                                                                'latereturnfine', 'dateoverdue', 'finalprice'),
                                          xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.config(command=self.library_table.xview)
        y_scroll.config(command=self.library_table.yview)

        self.library_table.heading('membertype', text="Member Type")
        self.library_table.heading('prnno', text="PRN No")
        self.library_table.heading('title', text="Title")
        self.library_table.heading('firstname', text="First Name")
        self.library_table.heading('lastname', text="Last Name")
        self.library_table.heading('address', text="Address1")
        self.library_table.heading('mobileid', text="Mobile ID")
        self.library_table.heading('bookid', text="Book ID")
        self.library_table.heading('booktitle', text="Book Title")
        self.library_table.heading('author', text="Author")
        self.library_table.heading('dateborrowed', text="Date Of Borrowed")
        self.library_table.heading('datedue', text="Date Due")
        self.library_table.heading('days', text="Days On Book")
        self.library_table.heading('latereturnfine', text="LateReturnFine")
        self.library_table.heading('dateoverdue', text="DateOverDue")
        self.library_table.heading('finalprice', text="Final Price")

        self.library_table.column('membertype', width=100)
        self.library_table.column('prnno', width=100)
        self.library_table.column('title', width=100)
        self.library_table.column('firstname', width=100)
        self.library_table.column('lastname', width=100)
        self.library_table.column('address', width=100)
        self.library_table.column('mobileid', width=100)
        self.library_table.column('bookid', width=100)
        self.library_table.column('booktitle', width=100)
        self.library_table.column('author', width=100)
        self.library_table.column('dateborrowed', width=100)
        self.library_table.column('datedue', width=100)
        self.library_table.column('days', width=100)
        self.library_table.column('latereturnfine', width=100)
        self.library_table.column('dateoverdue', width=100)
        self.library_table.column('finalprice', width=100)

        self.library_table["show"] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)
        self.fetcher_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    # ---------------------------------Functions_________________________________________
    def add_data(self):
        con = mysql.connector.connect(host="#####",
                                      user="root",
                                      passwd="####",
                                      database="l_data",
                                      port=3306,
                                      auth_plugin='mysql_native_password'
                                      )
        my_cursor = con.cursor()
        my_cursor.execute('insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                          (self.member_var.get(),
                           self.prn_var.get(),
                           self.id_var.get(),
                           self.firstname_var.get(),
                           self.lastname_var.get(),
                           self.address1_var.get(),
                           self.mobile_var.get(),
                           self.bookId_var.get(),
                           self.bookTitle_var.get(),
                           self.author_var.get(),
                           self.dateBorrowed_var.get(),
                           self.dateDue_var.get(),
                           self.dateOverDue.get(),
                           self.dateOnBook_var.get(),
                           self.lateFine_var.get(),
                           self.finalPrice_var.get(),
                           )
                          )
        con.commit()
        self.fetcher_data()
        con.close()
        messagebox.showinfo("Success", "Successfully added")

    def fetcher_data(self):
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="***",
                                      database="l_data",
                                      port=3306,
                                      auth_plugin='mysql_native_password'
                                      )
        my_cursor = con.cursor()
        my_cursor.execute('SELECT * from data ')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            con.commit()
            con.close()

    def get_cursor(self, event=''):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.bookId_var.set(row[7]),
        self.bookTitle_var.set(row[8]),
        self.author_var.set(row[9]),
        self.dateBorrowed_var.set(row[10]),
        self.dateDue_var.set(row[11]),
        self.dateOverDue.set(row[12]),
        self.dateOnBook_var.set(row[13]),
        self.lateFine_var.set(row[14]),
        self.finalPrice_var.set(row[15])

    def show_data(self):
        self.textbox.insert(END, "Member type:\t" + self.member_var.get() + "\n")
        self.textbox.insert(END, "PRN No\t" + self.prn_var.get() + "\n")
        self.textbox.insert(END, "ID No\t" + self.id_var.get() + "\n")
        self.textbox.insert(END, "First Name\t" + self.firstname_var.get() + "\n")
        self.textbox.insert(END, "Last Name\t" + self.lastname_var.get() + "\n")
        self.textbox.insert(END, "Address\t" + self.address1_var.get() + "\n")
        self.textbox.insert(END, "Mobile\t" + self.mobile_var.get() + "\n")
        self.textbox.insert(END, "Book id\t" + self.bookId_var.get() + "\n")
        self.textbox.insert(END, "Book Title\t" + self.bookTitle_var.get() + "\n")
        self.textbox.insert(END, "Author\t" + self.author_var.get() + "\n")
        self.textbox.insert(END, "Borrowed at\t" + self.dateBorrowed_var.get() + "\n")
        self.textbox.insert(END, "Due date\t" + self.dateDue_var.get() + "\n")
        self.textbox.insert(END, "Date Over due\t" + self.dateOverDue.get() + "\n")
        self.textbox.insert(END, "Dateonbook\t" + self.dateOnBook_var.get() + "\n")
        self.textbox.insert(END, "late fine\t" + self.lateFine_var.get() + "\n")
        self.textbox.insert(END, "Final price\t" + self.finalPrice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.mobile_var.set(""),
        self.bookId_var.set(""),
        self.bookTitle_var.set(""),
        self.author_var.set(""),
        self.dateBorrowed_var.set(""),
        self.dateDue_var.set(""),
        self.dateOverDue.set(""),
        self.dateOnBook_var.set(""),
        self.lateFine_var.set(""),
        self.finalPrice_var.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iexit > 0:
            self.root.destroy()
            return

    def update(self):
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="9101",
                                      database="l_data",
                                      port=3306,
                                      auth_plugin='mysql_native_password'
                                      )
        my_cursor = con.cursor()
        my_cursor.execute(
            'UPDATE data set member=%s,ID=%s,FirstName=%s,LastName=%s,Address=%s,MobileNo=%s,BookID=%s,'
            'BookTitle=%s,Author=%s,DateBorrow=%s,DateDue=%s,Dateoverdue=%s,DateOnbook=%s,lateFine=%s,'
            'finalprice=%s,PRNNO=%s',
            (
                self.member_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.mobile_var.get(),
                self.bookId_var.get(),
                self.bookTitle_var.get(),
                self.author_var.get(),
                self.dateBorrowed_var.get(),
                self.dateDue_var.get(),
                self.dateOverDue.get(),
                self.dateOnBook_var.get(),
                self.lateFine_var.get(),
                self.finalPrice_var.get(),
                self.prn_var.get(),
            ))
        con.commit()
        self.fetcher_data()
        self.reset()
        con.close()
        messagebox.showinfo("update", "Updated")

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "Select the member")
        else:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="9101",
                                          database="l_data",
                                          port=3306,
                                          auth_plugin='mysql_native_password'
                                          )
            my_cursor = con.cursor()
            query = "delete from data where PRNNO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            con.commit()
            self.fetcher_data()
            self.reset()
            con.close()
            messagebox.showinfo("info", "deleted")


if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
