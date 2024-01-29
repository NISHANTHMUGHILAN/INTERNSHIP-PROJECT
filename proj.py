import tkinter
from tkinter import *
from tkinter import messagebox

window=Tk()
def save():
    name=e1.get()
    doj=e2.get()
    age=e6.get()
    address=e3.get()
    contact=e4.get()
    email=e10.get()
    gender=e8.get()
    f=open("filenew2.txt","a")
    f.write("Name: ")
    f.write(name)
    f.write("\t")
    f.write("DOJ: ")
    f.write(doj)
    f.write("\t")
    f.write("Age: ")
    f.write(age)
    f.write("\t")
    f.write("Address: ")
    f.write(address)
    f.write("\t")
    f.write("Contact: ")
    f.write(contact)
    f.write("\t")
    f.write("Gender: ")
    f.write(gender)
    f.write("\t")
    f.write("E-mail: ")
    f.write(email)
    f.write("\t")
    f.write("\n")
    tkinter.messagebox.showinfo("","Information Saved Successfully")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    e10.delete(0,END)
    e8.delete(0,END)

def delete():
    file = open("filenew2.txt", "r")
    lines = file.readlines()
    new_lines = []
    n1=e1.get()
    n2=e2.get()
    n3=e3.get()
    n4=e4.get()
    n6=e6.get()
    n10=e10.get()
    n8=e8.get()
    for  line in lines:
       if n1 not in line.strip():
          new_lines.append(line)
       elif n2 not in line.strip():
            new_lines.append(line)
       elif n3 not in line.strip():
            new_lines.append(line)
       elif n4 not in line.strip():
            new_lines.append(line)
       elif n6 not in line.strip():
            new_lines.append(line)
       elif n10 not in line.strip():
            new_lines.append(line)
       elif n8 not in line.strip():
            new_lines.append(line)
    file.close()
    file = open("filenew2.txt", "w")
    file.writelines(new_lines)
    file.close()
    tkinter.messagebox.showinfo("","Information Deleted Successfully !!!!")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    e10.delete(0,END)
    e8.delete(0,END)
def view():
    tb.delete("1.0","end")
    filename = r"filenew2.txt"
    key =e1.get()
    with open(filename) as file:
            lines = file.readlines()
    e1.delete(0,END)
    """for number, line in enumerate(lines, 1): 
            if key not in line:
                    tb.insert('end',"not found")
                    break"""
    for number, line in enumerate(lines, 1): 
            if key in line:
                    tb.insert('end',line)
                    break   
"""    if(e1.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key1 =e1.get()
        with open(filename) as file:
            lines = file.readlines()
        e1.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key1 in line:
                tb.insert('end',line)
                break
                    
    if(e2.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key2 =e2.get()
        with open(filename) as file:
            lines = file.readlines()
        e2.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key2 in line:
                    tb.insert('end',line)
                    break
                    
    if(e3.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key3 =e3.get()
        with open(filename) as file:
            lines = file.readlines()
        e3.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key3 in line:
                    tb.insert('end',line)
                    break
    if(e4.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key4 =e4.get()
        with open(filename) as file:
            lines = file.readlines()
        e4.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key4 in line:
                    tb.insert('end',line)
                    break
    if(e6.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key5 =e6.get()
        with open(filename) as file:
            lines = file.readlines()
        e6.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key5 in line:
                    tb.insert('end',line)
                    break
    if(e10.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key7 =e10.get()
        with open(filename) as file:
            lines = file.readlines()
        e10.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key7 in line:
                    tb.insert('end',line)
                    break
    if(e8.get())!=0:
        tb.delete("1.0","end")
        filename = r"filenew2.txt"
        key8 =e8.get()
        with open(filename) as file:
            lines = file.readlines()
        e8.delete(0,END)
        for number, line in enumerate(lines, 1): 
            if key8 in line:
                    tb.insert('end',line)
                    break"""
                            

def update():
    if len(e1.get())!=0:
        search_text=e1.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    elif len(e2.get())!=0:
        search_text=e2.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}DOES NOT EXIST !!!!")
    elif len(e6.get())!=0:
        search_text=e6.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    elif len(e3.get())!=0:
        search_text=e3.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    elif len(e4.get())!=0:
        search_text=e4.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    elif len(e10.get())!=0:
        search_text=e10.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    elif len(e8.get())!=0:
        search_text=e8.get()
        replace_text=e7.get()
        with open(r'filenew2.txt', 'r') as file:
            data = file.read()
        if search_text in data: 
            data = data.replace(search_text, replace_text)
            tkinter.messagebox.showinfo(""," UPDATED SUCCESSFULLY !!!")
        elif search_text not in data:
            tkinter.messagebox.showinfo("",f"{search_text}  DOES NOT EXIST !!!!")
    with open(r'filenew2.txt', 'w') as file:
            file.write(data)
    e1.delete(0,END)
    e7.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    e10.delete(0,END)
    e8.delete(0,END)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    tb.delete("1.0","end")
    
l1=Label(window,text="Name :")
l1.grid(row=2,column=2)
e1=Entry()
e1.grid(row=2,column=3)

l6=Label(window,text="Gender :")
l6.grid(row=2,column=6)
e8=Entry()
e8.grid(row=2,column=7)

l2=Label(window,text="D.O.J :")
l2.grid(row=3,column=2)
e2=Entry()
e2.grid(row=3,column=3)

l7=Label(window,text="E-mail :")
l7.grid(row=3,column=6)
e10=Entry()
e10.grid(row=3,column=7)

l3=Label(window,text="Address :")
l3.grid(row=5,column=2)
e3=Entry()
e3.grid(row=5,column=3)

l4=Label(window,text="Contact No:")
l4.grid(row=4,column=6)
e4=Entry()
e4.grid(row=4,column=7)

l5=Label(window,text="Age :")
l5.grid(row=4,column=2)
e6=Entry()
e6.grid(row=4,column=3)


e7=Entry()
e7.grid(row=9,column=3)
b1=Button(window,text="Save",command=save)
b1.grid(row=8,column=4)

b2=Button(window,text="View",command=view)
b2.grid(row=8,column=6)

b3=Button(window,text="Update",command=update)
b3.grid(row=9,column=4)

b4=Button(window,text="Delete",command=delete)
b4.grid(row=9,column=6)

tb=Text(window,height=4,width=30)
tb.grid(row=8,column=25)

b5=Button(window,text="Clear",command=clear)
b5.grid(row=10,column=25)
window.mainloop()
