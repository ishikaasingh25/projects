# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_gen = "".join(password_list)
    password.insert(0, password_gen)
    pyperclip.copy(password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=Website.get()
    email=Email.get()
    pswd=password.get()
    if len(website) == 0 or len(email) == 0 or len(pswd) == 0:
        error = messagebox.showinfo(title="Some fields are empty",
                                    message="Please ensure all the fields are correctly filled")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered : \nEmail:{email} \nPassword:{pswd} \nIs is ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {pswd} \n")
                Website.delete(0, END)
                password.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password manager")
window.config(padx=30,pady=30,)

canvas=Canvas(width=300,height=200,highlightthickness=0)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=2)

Website_label=Label(text="Website:",font=("Arial",10,"bold"))
Website_label.grid(row=1,column=1)
Website=Entry(width=42)
Website.grid(row=1,column=2,columnspan=2)
Website.focus()

Email_label=Label(text="Email/Username:",font=("Arial",10,"bold"))
Email_label.grid(row=2,column=1)
Email=Entry(width=42)
Email.grid(row=2,column=2,columnspan=2)
Email.insert(0,"kuhoo25@gmail.com")

password_label=Label(text="Password:",font=("Arial",10,"bold"))
password_label.grid(row=3,column=1,)
password=Entry(width=42)
password.grid(row=3,column=2,columnspan=2)

generate_button=Button(text="Generate password",font=("Arial",10,"bold"),width=31,command=generate)
generate_button.grid(row=4,column=2)


add_button=Button(text="Add to file",font=("Arial",10,"bold"),width=31,command=save)
add_button.grid(row=5,column=2,columnspan=2)
window.mainloop()