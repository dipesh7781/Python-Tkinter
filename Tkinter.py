import tkinter as tk
window = tk.Tk()
window.title('GUI')

#Create Lables
name_label= tk.Label(window, text='Enter your name:')
name_label.grid(row=0, column=0, sticky=tk.W)

age_label= tk.Label(window, text= 'Enter your AGE:')
age_label.grid(row=1, column=0, sticky=tk.W)

email_label= tk.Label(window, text='Enter your Email:')
email_label.grid(row=2, column=0, sticky=tk.W)

#Create entery box
name_var = tk.StringVar()
name_entrybox= tk.Entry(window, width=15, textvariable = name_var)
name_entrybox.grid(row=0, column=1)

age_var = tk.StringVar()
age_entrybox= tk.Entry(window, width=15, textvariable=age_var)
age_entrybox.grid(row=1, column=1)

email_var = tk.StringVar()
email_entrybox= tk.Entry(window, width=15, textvariable=email_var )
email_entrybox.grid(row=2, column=1)


window.mainloop()




