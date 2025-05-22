from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *

license_list = read_from_file("license.dat")


def load_data(license_list):
    license_list = read_from_file("license.dat")
    for row in table.get_children():
        table.delete(row)

    for license in license_list:
        table.insert("", END, values=license)


def reset_form():
    id.set(len(license_list) + 1)
    name.set("")
    family.set("")
    license_number.set("")
    data.set("")
    license_type.set("")
    load_data(license_list)


def save_btn_click():
    license = (id.get(), name.get(), family.get(), license_number.get(),data.get(), license_type.get())
    errors = license_validator(license)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "license saved")
        license_list.append(license)
        write_to_file("license.dat", license_list)
        reset_form()


def table_select(x):
    selected_license = table.item(table.focus())["values"]
    if selected_license:
        id.set(selected_license[0])
        name.set(selected_license[1])
        family.set(selected_license[2])
        license_number.set(selected_license[3])
        data.set(selected_license[4])
        license_type.set(selected_license[5])



#def edit_btn_click():
 #   pass


#def remove_btn_click():
 #   pass#


window = Tk()
window.title("Person Info")
window.geometry("610x270")

# Id
Label(window, text="Id").place(x=20, y=10)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=10)

# Name
Label(window, text="Name").place(x=20, y=35)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=35)

# Family
Label(window, text="Family").place(x=20, y=60)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=60)

# License Number
Label(window, text="License Number").place(x=5, y=85)
license_number = StringVar()
Entry(window, textvariable=license_number).place(x=100, y=85)

# Data
Label(window, text="Data").place(x=20, y=110)
data = StringVar()
Entry(window, textvariable=data).place(x=100, y=110)

# License Type
Label(window, text="License Type").place(x=20, y=135)
license_type= StringVar()
Entry(window, textvariable=license_type).place(x=100, y=135)

table = ttk.Treeview(window, columns=[1, 2, 3, 4,5,6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="License Number")
table.heading(5, text="Data")
table.heading(6, text="License Type")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
#Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
#Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()

window.mainloop()