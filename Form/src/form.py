import tkinter as tk

from service_form import save_form


root=tk.Tk()
root.geometry("300x400")

#Function
def saveInfo():
    data ={
        "name": first_name,
        "lastName": last_name,
        "phone":phone,
        "email":email,
        "address":address
    }
    save_form(data=data)
#variables
data = {}

first_name= tk.Entry(root)
last_name= tk.Entry(root)
email= tk.Entry(root)
phone= tk.Entry(root)
address= tk.Entry(root)

label_name= tk.Label(root,text="First Name")
label_last=tk.Label(root,text="Last Name")
label_email=tk.Label(root,text="Email")
label_phone=tk.Label(root,text="Phone")
label_address= tk.Label(root,text="Address")

first_name.grid(row=0,column=1)
last_name.grid(row=1,column=1)
email.grid(row=2,column=1)
phone.grid(row=3,column=1)
address.grid(row=4,column=1)

label_name.grid(row=0,column=0)
label_last.grid(row=1,column=0)
label_email.grid(row=2,column=0)
label_phone.grid(row=3,column=0)
label_address.grid(row=4,column=0)


btn_save = tk.Button(root,text="SAVE", command=saveInfo)
btn_save.grid()


root.mainloop()