import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title('Data Entry Form')

window.geometry('600x300')

frame = tk.Frame(window)
frame.pack()

user_info = tk.LabelFrame(frame, text='User Information')
user_info.grid(row=1, column=1, padx=20,pady=20)

name = tk.Label(user_info, text='Name')
name.grid(row=1, column=1)
name_entry = tk.Entry(user_info)
name_entry.grid(row=2,column=1)
email = tk.Label(user_info, text='Email')
email.grid(row=3, column=1)
email_entry = tk.Entry(user_info)
email_entry.grid(row=4,column=1)

title_label = tk.Label(user_info, text='Title')
title_combobox = ttk.Combobox(user_info, value=['','First','Second','Third'])
title_label.grid(row=1,column=2)
title_combobox.grid(row=2,column=2)

age_label = tk.Label(user_info, text='Age')
age_spinbox = tk.Spinbox(user_info, from_=18, to=110)
age_label.grid(row=5,column=1)
age_spinbox.grid(row=6, column=1)

nationality_label = tk.Label(user_info, text='Nationality')
nationality_label.grid(row=3,column=2)
nationality_combobox = ttk.Combobox(user_info, values=['','Africa','Europe','Antartica','Asia','Oceania','North/South America'])
nationality_combobox.grid(row=4,column=2)

for widget in user_info.winfo_children():
     widget.grid_configure(padx=10,pady=5)
     
another_frame = tk.LabelFrame(frame, text='Adition')
another_frame.grid(row=1,column=2, padx=20,pady=20) 

movie = tk.Label(another_frame, text='Movies you like')
movie.grid(row=1,column=1)
movie_combobox = ttk.Combobox(another_frame, value=['','Marvel','StarWars','Avatar'])
movie_combobox.grid(row=2,column=1) 

languages = tk.Label(another_frame, text='Languages you know')
languages.grid(row=3,column=1)
languages_select = ttk.Checkbutton(another_frame, text='English')
languages_select.grid(row=4, column=1)
languages_select = ttk.Checkbutton(another_frame, text='Franch')
languages_select.grid(row=5,column=1)
languages_select = ttk.Checkbutton(another_frame, text='Spanish')
languages_select.grid(row=6,column=1)

studies = tk.Label(another_frame, text='Studies')
studies.grid(row=7,column=1)
studies_select = ttk.Combobox(another_frame, values=['','Informatics','Computer Science','Another'])
studies_select.grid(row=8,column=1)

button = tk.Button(window, text='Submit')
button.pack()

window.mainloop()