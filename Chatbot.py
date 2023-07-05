from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root123@")
mycursor = mydb.cursor()
mycursor.execute("use shop")

def Register():
        def Submit():
                it = "insert into customer values ( %s, %s)"
                val = (t3.get(), t4.get())
                mycursor.execute(it, val)
                mydb.commit()
                reg.destroy()
                
        reg = Toplevel()
        reg.title("Registration Window")
        l3 = Label(reg, text = "Name: ")
        l4 = Label(reg, text = "Password: ")
        t3 = Entry(reg)
        t4 = Entry(reg)
        b3 = Button(reg, text = "Submit", command = Submit)

        l3.grid(row = 0, column = 0)
        l4.grid(row = 2, column = 0)
        t3.grid(row = 0, column = 2)
        t4.grid(row = 2, column = 2)
        b3.grid(row = 4, column = 0)

def Login():
        sel = "select * from customer where name = %s and password = %s"
        val1 = (t1.get(), t2.get())
        mycursor.execute(sel, val1)
        temp = mycursor.fetchall()
        if temp:
                root1.destroy()
                root = Tk()
                root.title("Chatbot")

                BG_GRAY = "#CD9C8A"
                BG_COLOR = "#FF5100"
                TEXT_COLOR = "#FFFFFF"

                FONT = "Helvetica 14"
                FONT_BOLD = "Helvetica 13 bold"

                def send():
                        send = "You -> " + e.get()
                        txt.insert(END, "\n" + send)

                        user = e.get().lower()

                        if (user == "hello"):
                                txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
                 
                        elif (user == "hi" or user == "hii" or user == "hiiii"):
                                txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

                        elif (user == "list"):
                                txt.insert(END, "\n" + "Bot -> Lists are used to store multiple items in a single variable.\nLists are created using square brackets.\nList items are ordered, changeable, and allow duplicate values.")

                        elif (user == "tuple"):
                                txt.insert(END, "\n" + "Bot -> Tuples are used to store multiple items in a single variable.\nA tuple is a collection which is ordered and unchangeable.\nTuples are written with round brackets.")

                        elif (user == "dictionary"):
                                txt.insert(END, "\n" + "Bot -> Dictionaries are used to store data values in key: value pairs.\nA dictionary is a collection which is ordered, changeable and do not allow duplicates.\nDictionaries are written with curly brackets, and have keys and values.")

                        elif (user == "set"):
                                txt.insert(END, "\n" + "Bot -> Sets are used to store multiple items in a single variable.\nA set is a collection which is unordered, unchangeable, and unindexed.\nSet items are unchangeable, but you can remove items and add new items.\nSets are written with curly brackets.")

                        elif (user == "recursive function"):
                                txt.insert(END, "\n" + "Bot -> Recursion is the process of defining something in terms of itself.\nIn Python, we know that a function can call other functions.\nIt is even possible for the function to call itself.\nThese types of functions are termed as recursive functions.")

                        elif (user == "lambda function" or user == "lambda"):
                                txt.insert(END, "\n" + "Bot -> A lambda function is a small anonymous function.\nA lambda function can take any number of arguments, but can only have one expression. ")

                        elif (user == "map function" or user == "map"):
                                txt.insert(END, "\n" + "Bot -> map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.).")

                        elif (user == "thanks" or user == "thank you" or user == "now its my time"):
                                txt.insert(END, "\n" + "Bot -> My pleasure !")

                        elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
                                txt.insert(END, "\n" + "Bot -> Why does Python live on land?  Because it is above C level! ")

                        elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
                                txt.insert(END, "\n" + "Bot -> Have a nice day!")
                                root.destroy()

                        else:
                                txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

                        e.delete(0, END)

                lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

                txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
                txt.grid(row=1, column=0, columnspan=2)

                scrollbar = Scrollbar(txt)
                scrollbar.place(relheight=1, relx=0.974)

                e = Entry(root, bg="#CD9C8A", fg=TEXT_COLOR, font=FONT, width=55)
                e.grid(row=2, column=0)

                send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)

                root.mainloop()
        else:
                inva = Toplevel()
                l6 = Label(inva, text = "Invalid Username and Password")
                l6.grid(row = 0, column = 0)
                

root1 = Tk()
root1.title("Login")
l1 = Label(root1, text = "Name: ")
l2 = Label(root1, text = "Password: ")
t1 = Entry(root1)
t2 = Entry(root1, show = "*")
b1 = Button(root1, text = "Register", command = Register)
b2 = Button(root1, text = "Login", command = Login)

l1.grid(row = 0, column = 0)
l2.grid(row = 2, column = 0)
t1.grid(row = 0, column = 2)
t2.grid(row = 2, column = 2)
b1.grid(row = 4, column = 0)
b2.grid(row = 4, column = 2)

root1.mainloop()
