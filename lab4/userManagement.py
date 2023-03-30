import tkinter as tk
from lbs.writeToFile import write

def get_data():
    username = user_text.get()
    password = pass_text.get()
    write('userData.txt', f'{username}, {password}\n')

root = tk.Tk()

root.title('User Management')
root.geometry('500x300')
root.config(background='gray')

user_label = tk.Label(root, text='Username:', font=('Arial', 18))
user_label.pack(padx=10,pady=10)
user_text = tk.Entry(root, width=30)
user_text.pack(padx=10,pady=10)

pass_label = tk.Label(root, text=('Password:'), font=('Arial', 18))
pass_label.pack(padx=10,pady=10)
pass_text = tk.Entry(root, width=30, show='*')
pass_text.pack(padx=10,pady=10)

button = tk.Button(root, text='Submit', font=('Arial', 16), activebackground='gray', activeforeground='white', command=get_data)
button.pack(pady=10)

root = tk.mainloop()