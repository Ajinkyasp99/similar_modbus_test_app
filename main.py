from tkinter import *
import tkinter as tk
from tkinter import messagebox


class InitialPage:
    def __init__(self, test_app):
        self.test_app = test_app
        self.test_app.geometry("900x650")
        self.test_app.title("Enerlly Plant Onboard App")


test_tcp = Tk()
test_tcp.title("Enerlly Plant Onboard App")
test_tcp.iconbitmap("enerlly-logo.ico")
# p1 = PhotoImage(file="enerlly.ico")
# test_tcp.iconphoto(True, p1)
# test_tcp.resizable(0, 0)
# obj = InitialPage(test_tcp)
#
# test_tcp.rowconfigure(0, minsize=800, weight=1)
# test_tcp.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tk.Text(test_tcp)
# frm_buttons = tk.Frame(test_tcp, relief=tk.RAISED, bd=2, background="lightblue")
# btn_open = tk.Button(frm_buttons, text="Open")
# btn_save = tk.Button(frm_buttons, text="Save As...")
#
# btn_open.grid(row=0, column=0, sticky="ew", padx=30, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=30)
#
# frm_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")


def our_command():
    hide_all_frames()
    # l.destroy()
    # l.pack_forget()

    pass


def test_modbus_tcp_ip():
    frame3.pack_forget()
    frame1.pack_forget()
    frame2.pack(fill="both", expand=1)


def test_series():
    frame3.pack_forget()
    frame2.pack_forget()
    frame1.pack(fill="both", expand=1)
    # frame1.pack_forget()
    # l = Label()
    # l.grid(row=15, column=50)
    # l1 = Label()
    # l1.grid(row=2, column=0)
    # l2 = Label()
    # l2.grid(row=3, column=0)
    # l1 = Label(text="Choose Travel:", fg="Black", font=("calibre", 8, 'bold'), bg="lightGreen")
    # l1.grid(row=6, column=1, pady=5)


my_menu = Menu(test_tcp)
test_tcp.config(menu=my_menu)

# file_menu = Menu(my_menu)
my_menu.add_cascade(label="Modbus Test Serial", command=test_series)
my_menu.add_cascade(label="Modbus Test TCP IP", command=test_modbus_tcp_ip)
my_menu.add_cascade(label="Create Device json", command=our_command)
# file_menu.add_command(label="Test Series", command=our_command)

frame1 = Frame(test_tcp, background="black",  height=750, width=1000)
frame2 = Frame(test_tcp, bg="blue",  height=750, width=1000)
frame3 = Frame(test_tcp, bg="lightGreen",  height=750, width=1000)


def hide_all_frames():
    frame1.pack_forget()
    frame3.pack_forget()
    frame2.pack_forget()


test_tcp.mainloop()
