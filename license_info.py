from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from license import License
from validator import *

license_list = read_from_file("license.dat")


def load_data(license_list):
    license_list = read_from_file("license.dat")
    for row in table.get_children():
        table.delete(row)

    for license in license_list:
        table.insert("", END, values=license.to_tuple())


def reset_form():
    id.set(len(license_list) + 1)
    name.set("")
    family.set("")
    license_number.set("")
    license_date.set("")
    license_type.set("")
    load_data(license_list)


def save_btn_click():
    license = License(id.get(), name.get(), family.get(), license_number.get(), license_date.get(), license_type.get())
    errors = license.validate()
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "license saved")
        license_list.append(license)
        write_to_file("license.dat", license_list)
        reset_form()


def table_select(x):
    selected_license = License(*table.item(table.focus())["values"])
    if selected_license:
        id.set(selected_license.id)
        name.set(selected_license.name)
        family.set(selected_license.family)
        license_number.set(selected_license.license_number)
        license_date.set(selected_license.license_date)
        license_type.set(selected_license.license_type)


def edit_btn_click():
    selected_item = table.focus()
    if not selected_item:
        msg.showwarning("Select Record", "Please select a record to edit.")
        return

    new_license = (id.get(), name.get(), family.get(), license_number.get(), license_date.get(), license_type.get())
    errors = license_validator(new_license)
    if errors:
        msg.showerror("Validation Error", "\n".join(errors))
        return

    for index in range(len(license_list)):
        if str(license_list[index][0]) == str(new_license[0]):
            license_list[index] = new_license
            break

    write_to_file("license.dat", license_list)
    msg.showinfo("Updated", "License info updated successfully.")
    reset_form()


def remove_btn_click():
    selected_item = table.focus()
    if selected_item:
        selected_license = table.item(selected_item)["values"]
        new_list = []
        for item in license_list:
            if item[0] != selected_license[0]:
                new_list.append(item)
        license_list[:] = new_list
        write_to_file("license.dat", license_list)
        reset_form()
    else:
        msg.showwarning("Select Record", "Please select a record to remove.")
        return


window = Tk()
window.title("license Info")
window.geometry("900x270")

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
Label(window, text="Date").place(x=20, y=110)
license_date = StringVar()
Entry(window, textvariable=license_date).place(x=100, y=110)

# License Type
Label(window, text="License Type").place(x=20, y=135)
license_type = StringVar()
Entry(window, textvariable=license_type).place(x=100, y=135)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
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
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()

window.mainloop()
