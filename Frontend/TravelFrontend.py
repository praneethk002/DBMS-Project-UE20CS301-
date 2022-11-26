import tkinter 
import customtkinter
from PIL import Image
# import travels_backend as bk
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import Listbox
import mysql.connector
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()

app.geometry("780x520")
app.title("Praneeth Travel Services")
def button_callback():
    print(User_name.get())

global l
l = []

Phone_number = ""
Address = ""


def Insert():
    name = User_name.get()
    phone = Phone_number.get()
    address = Address.get()
    cid = "4011"
    if (cid == "" or name == "" or phone == "" or address == ""):
        messagebox.showinfo("Error", "Please fill all the fields")
    else:
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Travel")
        cursor = con.cursor()

        sql = "Insert into Customer(CID,CName, CAddress, CPhone) values ('"+cid+"','"+name+"', '"+address+"', '"+phone+"')"
        cursor.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("Insert Status", "Inserted Successfully")
def Delete():
    name = User_name.get()
    if (name == ""):
        messagebox.showinfo("Error", "Please Enter Name")
    else:
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Travel")
        cursor = con.cursor()
        sql = "Delete from Customer where CName = '"+name+"'"
        cursor.execute(sql)
        con.commit()
        con.close()

        messagebox.showinfo("Delete Status", "Deleted Successfully")
def Update():
    name = User_name.get()
    phone = Phone_number.get()
    address = Address.get()
    if (name == "" ):
        messagebox.showinfo("Error", "Please Enter Name")
    
    else:
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Travel")
        cursor = con.cursor()
        sql = "Update Customer set CAddress ='"+address+"' where CName ='"+name+"'"
        cursor.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("Update Status", "Updated Successfully")
def Search():
    name = User_name.get()
    if (name == ""):
        messagebox.showinfo("Error", "Please Enter Name")
    else:
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Travel")
        cursor = con.cursor()
        sql = "Select * from Customer where CName = '"+name+"'"
        cursor.execute(sql)
        result = cursor.fetchall()
        # con.commit()
        con.close()

        if (result == []):
            messagebox.showinfo("Search Status", "No Record Found")
        else:
            messagebox.showinfo("Search Status", "Record Found") 
            return result

def Display():
    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Travel")
    cursor = con.cursor()
    sql = "Select * from Customer"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        data = str(row[0])+'\t'+str(row[1])+'\t'+str(row[2])+'\t'+str(row[3])+'\n'
        List.insert(tkinter.END, data)
        # s+= "CID: "+str(row[0])+" CName: "+str(row[1])+" CAddress: "+str(row[2])+" CPhone: "+str(row[3])+"\n"
    # textbox.insert("0.0",s)
    # messagebox.showinfo("The Records are", s)
    con.commit()
    con.close()
        
def Clear():
    User_name = customtkinter.CTkEntry( placeholder_text="Enter Username",text_font=("Helvetica Neue", 10),width = 200)
    User_name.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    Phone_number = customtkinter.CTkEntry( placeholder_text="Enter Phone_Number",text_font=("Helvetica Neue", 10),width = 200)
    Phone_number.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    Address = customtkinter.CTkEntry( placeholder_text="Enter Address",text_font=("Helvetica Neue", 10),width = 200)
    Address.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)
    List.delete(0, tkinter.END)
text_var = tkinter.StringVar(value="Travel Agency")

label_1 = customtkinter.CTkLabel(corner_radius=50,justify=tkinter.CENTER,textvariable=text_var,text_font=("Helvetica Neue", 55))
label_1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
text_var3 = tkinter.StringVar(value="Welcome To Praneeth Travels")
label_2 = customtkinter.CTkLabel(corner_radius=50, justify=tkinter.CENTER,textvariable=text_var3,text_font=("Helvetica Neue", 23))
label_2.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
text_var4 = tkinter.StringVar(value="Most Affordable Rides in the City")
label_2 = customtkinter.CTkLabel(corner_radius=50, justify=tkinter.CENTER,textvariable=text_var4,text_font=("Helvetica Neue", 10))
label_2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


my_image = tkinter.PhotoImage(file = "/Users/praneethkumar/Documents/SEM5/DBMS/PES2UG20CS251_Project/Project/taxi.png")

button10 = customtkinter.CTkLabel(app, image=my_image)
button10.configure(width=5,height=5)
button10.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# text_var5 = tkinter.StringVar(value="Enter Name")
# label_2 = customtkinter.CTkLabel(corner_radius=50, justify=tkinter.CENTER,textvariable=text_var4,text_font=("Helvetica Neue", 10))
# label_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# list = Listbox(master = app, height=150, width=300)
# Listbox.place(relx=0.7, rely=0.6)
scrollbar=Scrollbar(app)
scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

List=Listbox(app,font=('Helvetica Neue',12,),bg="#373b3d", width = 40, height = 10,yscrollcommand=scrollbar.set)
# List.bind('<<ListboxSelect>>',Records)
List.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
# List.grid(row=0,column=0,padx=10)
scrollbar.config(command= List.yview)


#   insert at line 0 character 0
# text = textbox.cget( "0")  # get text from line 0 character 0 till the end

# textbox.configure(state="disabled",width=300, height=150, text_font=("Helvetica Neue", 10)) 
# textbox.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)


User_name = customtkinter.CTkEntry( placeholder_text="Enter Username",text_font=("Helvetica Neue", 10),width = 200)
User_name.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

Phone_number = customtkinter.CTkEntry( placeholder_text="Enter Phone_Number",text_font=("Helvetica Neue", 10),width = 200)
Phone_number.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
Address = customtkinter.CTkEntry( placeholder_text="Enter Address",text_font=("Helvetica Neue", 10),width = 200)
Address.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

Btn_txt1 = tkinter.StringVar(value="Insert")
inser_btn = customtkinter.CTkButton(textvariable=Btn_txt1, command=Insert)
inser_btn.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)

Btn_txt2 = tkinter.StringVar(value="Display")
Disp_btn = customtkinter.CTkButton(textvariable=Btn_txt2, command=Display)
Disp_btn.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)

Btn_txt3 = tkinter.StringVar(value="Clear")
Clear_btn = customtkinter.CTkButton(textvariable=Btn_txt3, command=Clear)
Clear_btn.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

Btn_txt4 = tkinter.StringVar(value="Delete")
Delete_btn = customtkinter.CTkButton(textvariable=Btn_txt4, command=Delete)
Delete_btn.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)

Btn_txt5 = tkinter.StringVar(value="Update")
Update_btn = customtkinter.CTkButton(textvariable=Btn_txt5, command=Update)
Update_btn.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)
print(l)
app.mainloop()
