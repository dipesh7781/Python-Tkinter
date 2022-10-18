import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Basic GUI")

 #Label
Name_Label= ttk.Label(window, text="Name")
Name_Label.grid(row=0, column=0, sticky=tk.W)

Age_Label= ttk.Label(window,text="Age")
Age_Label.grid(row=1,column=0, sticky=tk.W)

Cmb_Label= ttk.Label(window,text="Gender")
Cmb_Label.grid(row=2, column=0,sticky=tk.W)

#EntryBoc
nameV= tk.StringVar()
Name_Entry= ttk.Entry(window,width=12, textvariable=nameV)
Name_Entry.grid(row=0, column=1)

ageV= tk.StringVar()
Age_Entry=ttk.Entry(window,width=12, textvariable=ageV)
Age_Entry.grid(row=1, column=1)

#Comboox
cmbV= tk.StringVar()
cmb_gender= ttk.Combobox(window, width=12, state='readonly',textvariable=cmbV)
cmb_gender['values']= ('male', 'female', 'gender')
cmb_gender.current(0)
cmb_gender.grid(row=2, column=1)

#Radio Button
radioSV= tk.StringVar()
radiobtn1= ttk.Radiobutton(window, text="Student", value='student',variable=radioSV)
radiobtn1.grid(row=3, column=0)

radiobtn2= ttk.Radiobutton(window, text="Teacher", value='Teacher', variable=radioSV)
radiobtn2.grid(row=3, column=1)

#Check Boc
chkbtnv=tk.IntVar()
chkBox= ttk.Checkbutton(window, text="Subscribe for more", variable=chkbtnv)
chkBox.grid(row=4, columnspan=3)

#Button
def action():
 Username= nameV.get()
 Userage= ageV.get()
 Usergender=cmbV.get()
 Userrole= radioSV.get()
 Usercheck=chkbtnv.get()
 if chkbtnv. get()== 0:
     subscribe='NO'
 else:
     subscribe='YES'

 print(f'His Name is {Username} and his age is {Userage} {Usergender}{Userrole}{Usercheck} {subscribe}')

Submit_Btn= tk.Button(window, width=10, text="Submit", command=action)
Submit_Btn.grid(row=5, column=1)

window.mainloop()