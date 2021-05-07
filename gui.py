from tkinter import *
import os
from PIL import Image, ImageTk
import time

# main screen
master = Tk()
master.title("Banking App")

# register finish function
def finish():
    name =temp_name.get()
    age =temp_age.get()
    phone =temp_phone.get()
    password  =temp_password.get()
    all_accounts = os.listdir()

    if name =="" or age =="" or phone=="" or password=="":
        notify.config(fg="red" , text="All fields required *")
        return
     
    for name_check in all_accounts:
        if name == name_check:
            notify.config(fg="red" , text="Account already exists")
            return 

        else:
            new_file = open(name ,"w")
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(phone+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()

            notify.config(fg="green" , text ="Account has been created")
            reg_screen.destroy() 

# register function 
def register():
    global temp_name
    global temp_age
    global temp_phone
    global temp_password
    global notify
    global reg_screen
   
    temp_name = StringVar()
    temp_age = StringVar()
    temp_phone = StringVar()
    temp_password = StringVar()
    reg_screen = Toplevel(master)
    reg_screen.title("Register")

    # labels
    Label(reg_screen, text="Lets get you register in most trusted Banking System",
          font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
    Label(reg_screen, text="Name", font=("Calibri", 14)).grid(row=1, sticky=W)
    Label(reg_screen, text="Age", font=("Calibri", 14)).grid(row=2, sticky=W)
    Label(reg_screen, text="PhoneNo.", font=(
        "Calibri", 14)).grid(row=3, sticky=W)
    Label(reg_screen, text="Password", font=(
        "Calibri", 14)).grid(row=5, sticky=W)
    notify = Label(reg_screen ,font=("Calibri", 14))
    notify.grid(row =7 , sticky=N , pady=10)


    # entries
    Entry(reg_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(reg_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(reg_screen, textvariable=temp_phone).grid(row=3, column=0)
    Entry(reg_screen, textvariable=temp_password,
          show="*").grid(row=5, column=0)

    # buttons
    Button(reg_screen, text='Register', font=('Calibri', 12), command=finish).grid(row=6, sticky=N, pady=10)

#login valdate
def login_session():
    global login_name
    all_account = os.listdir()
    login_name =temp_uname.get()
    login_password = temp_ppassword.get()

    for name in all_account:
        if name == login_name:
            filee = open(name,"r")
            file_data = filee.read()
            file_data = file_data.split('\n')
            password = file_data[3]
            if login_password == password:
                log_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")

                #labesl
                Label(account_dashboard, text="Account Dashboard",font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Welcome",font=("Calibri", 14)).grid(row=1, sticky=N, pady=10)

                #buttons
                Button(account_dashboard, text="Personal Details",font=("Calibri", 14),width=30, command=personal_details).grid(row=2, sticky=N, padx=10)
                Button(account_dashboard, text="Deposit",font=("Calibri", 14),width=30, command=deposit).grid(row=3, sticky=N, padx=10)
                Button(account_dashboard, text="Withdraw",font=("Calibri", 14),width=30, command = withdraw).grid(row=4, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notify.config(fg="red", text="Password Incorrect!!")
                return
    login_notify.config(fg="red" , text ="No account found")

def deposit():
    #vars
    global amount
    global deposit_notify
    global current_balance_label
    amount = StringVar()
    filee = open(login_name, "r")
    file_data = filee.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #deposit screen 
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")

    #labels
    Label(deposit_screen, text ="Deposit",font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen , text="Current Balance : $" + details_balance , font =("Calibri", 14))
    current_balance_label.grid(row=1 , sticky=W)
    Label(deposit_screen, text ="Amount : ",font=("Calibri", 14)).grid(row=2, sticky=W)
    deposit_notify = Label(deposit_screen , font = ("Calibri", 14))
    deposit_notify.grid(row=4 , sticky=N , pady=5)

    #enrty
    Entry(deposit_screen , textvariable = amount).grid(row=2, column=1)

    #button
    Button(deposit_screen ,text = "Finish" , font = ("Calibri", 14), command = finish_deposit).grid(row=3, sticky=W , pady=5)

def finish_deposit():
    if amount.get() == "":
        deposit_notify.config(text="Amount is required", fg="red")
        return

    if float(amount.get())<=0:
        deposit_notify.config(text="Negative or zero amount is not accepted" , fg="red")
        return

    filee =open(login_name , "r+")
    file_data = filee.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance , str(updated_balance))
    filee.seek(0)
    filee.truncate(0)
    filee.write(file_data)
    filee.close()

    current_balance_label.config(text="Current Balance : $"+str(updated_balance) , fg="green")
    deposit_notify.config(text="Balance Updated" , fg="green")



def withdraw():
    global withdraw
    global withdraw_notify
    global current_balance_label
    withdraw = StringVar()
    filee = open(login_name, "r")
    file_data = filee.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #deposit screen 
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")

    #labels
    Label(withdraw_screen, text ="Withdraw",font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen , text="Current Balance : $" + details_balance , font =("Calibri", 14))
    current_balance_label.grid(row=1 , sticky=W)
    Label(withdraw_screen, text ="Amount : ",font=("Calibri", 14)).grid(row=2, sticky=W)
    withdraw_notify = Label(withdraw_screen , font = ("Calibri", 14))
    withdraw_notify.grid(row=4 , sticky=N , pady=5)

    #enrty
    Entry(withdraw_screen , textvariable = withdraw).grid(row=2, column=1)

    #button
    Button(withdraw_screen ,text = "Withdraw" , font = ("Calibri", 14), command = finish_withdraw).grid(row=3, sticky=W , pady=5)


def finish_withdraw():
    if withdraw.get() == "":
        withdraw_notify.config(text="withdraw amount is required", fg="red")
        return

    if float(withdraw.get())<=0:

        withdraw_notify.config(text="Negative or zero amount is not accepted" , fg="red")
        return
    
    
    filee =open(login_name , "r+")
    file_data = filee.read()
    details = file_data.split('\n')
    current_balance = details[4]
    if float(withdraw.get() > float(current_balance)):
        withdraw_notify.config(text="Insufficeint funds" , fg="red")
        return
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw.get())
    file_data = file_data.replace(current_balance , str(updated_balance))
    filee.seek(0)
    filee.truncate(0)
    filee.write(file_data)
    filee.close()

    current_balance_label.config(text="Current Balance : $"+str(updated_balance) , fg="green")
    withdraw_notify.config(text="Balance Updated" , fg="green")

    



def personal_details():
    filee = open(login_name, "r")
    file_data = filee.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[1]
    details_phone = user_details[2]
    details_balance = user_details[4]

    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")

    #labels
    Label(personal_details_screen, text="WELCOME ",font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name: "+details_name,font=("Calibri", 14)).grid(row=1, sticky=W, pady=10)
    Label(personal_details_screen, text="Age: "+details_age,font=("Calibri", 14)).grid(row=2, sticky=W, pady=10)
    Label(personal_details_screen, text="Phone: "+details_phone,font=("Calibri", 14)).grid(row=3, sticky=W, pady=10)
    Label(personal_details_screen, text="Balance: $"+details_balance,font=("Calibri", 14)).grid(row=4, sticky=W, pady=10)

#login function
def login():
    global temp_uname
    global temp_ppassword
    global log_screen
    global login_notify
    temp_uname = StringVar()
    temp_ppassword = StringVar()
    log_screen = Toplevel(master)
    log_screen.title("Login")

    #labels
    Label(log_screen, text="Login here",
          font=("Calibri", 12)).grid(row=0, sticky=N, pady=10, padx=15)
    Label(log_screen, text="Username", font=("Calibri", 12)).grid(row=1, sticky=W, padx=15)
    Label(log_screen, text="Password", font=("Calibri", 12)).grid(row=2, sticky=W, padx=15)
    login_notify =Label(log_screen , font=("Calibri",12))
    login_notify.grid(row=4 , sticky=N)

    #entry
    Entry(log_screen , textvariable =temp_uname).grid(row=1, column =1, padx=5)
    Entry(log_screen , textvariable = temp_ppassword, show="*").grid(row=2 , column =1 , padx=5)   

    #button
    Button(log_screen , text='login' , command=login_session ,width=15, font=("Calibri" , 12)).grid(row=3, sticky=W, padx=5, pady=5)

# image import
img=Image.open("img.png")
img=img.resize((150, 150))
img=ImageTk.PhotoImage(img)

# labels
Label(master, text="Custom Banking Beta", font=(
    "Calibri", 14)).grid(row=0, sticky=N, pady=10)
Label(master, text="Worlds best banking system you will ever",
      font=("Calibri", 12)).grid(row=1, sticky=N , padx=15)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

# buttons
Button(master, text="Register", font=('Calibri', 12),
       width=20, command=register).grid(row=3, sticky=N)
Button(master, text="Login", font=('Calibri', 12), width=20,
       command=login).grid(row=4, sticky=N, pady=5)

master.mainloop()
