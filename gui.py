import tkinter as tk
from tkinter import ttk

#from Tkinter.Tkinter import action
window= tk.Tk()
window.title("Basic GUI")

#Create Label
name_Label= ttk.Label(window, text="Enter name")
name_Label.grid(row=0, column=0, sticky=tk.W)

age_Label= ttk.Label(window, text= "Enter your age")
age_Label.grid(row=1, column=0, sticky=tk.W)

combo_Label= ttk.Label(window, text="Select your age")
combo_Label.grid(row=2, column=0, sticky=tk.W)

#EntryBoc
nameV= tk.StringVar()
name_Entry= ttk.Entry(window, width=15, textvariable= nameV)
name_Entry.grid(row=0, column=1)
name_Entry.focus()

ageV= tk.StringVar()
age_Entry=ttk.Entry(window, width=15, textvariable= ageV)
age_Entry.grid(row= 1, column=1)

#create combobox

gender_var = tk.StringVar()
gender_combo = ttk.Combobox(window, width=12, textvariable=gender_var,state='readonly')
gender_combo['values'] = ('male', 'female', 'other')
gender_combo.current(0)
gender_combo.grid(row=2, column=1)
#RadioButton
userType=tk.StringVar()
radioBtn1= ttk.Radiobutton(window,text="Student", value='student', variable=userType)
radioBtn1.grid(row=3, column=0)

radioBtn2=ttk.Radiobutton(window, text="Teacher",value='teacher', variable=userType)
radioBtn2.grid(row=3, column=1)

#CHeck Button
checkbtn_var= tk.IntVar()
checkbtn=ttk.Checkbutton(window, text='CHeck if you want to subscribe my channel', variable=checkbtn_var)

checkbtn.grid(row=4, columnspan=3)


#Button
def action():
 username=nameV.get()
 userage= ageV.get()
 usergender= gender_var.get()
 usertype= userType.get()
 if checkbtn_var.get()==0:
  subscribed='NO'
 else:
  subscribed='YES'


 print(f'{username}is {userage} years old {usergender} is his gender{usertype} {subscribed}')

buttonB=tk.Button(window,text="Submt", width=10, command=action)
buttonB.grid(row=8, column=0)

window.mainloop()