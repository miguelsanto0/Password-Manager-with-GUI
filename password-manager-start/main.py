from tkinter import *
from tkinter import messagebox, Entry
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    
    letter_list = [random.choice(letters) for items in range(0, nr_letters)]
    symbols_list = [random.choice(symbols) for items in range(0,nr_symbols)]
    number_list = [random.choice(numbers) for num in range(0,nr_numbers)]
    
    password_list = letter_list + symbols_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    print(password)
    if len(password_input.get()) == 0:
        password_input.insert(0,password)
        pyperclip.copy(str(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():


    if len(website_user_input.get()) == 0 or len(email_username_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Dont leave any fields empty!")
    else:
        valid = messagebox.askokcancel(title=website_user_input.get(), message=f"These are the details entered: \nEmail/Username: {email_username_input.get()}\n Password: {password_input.get()}\n")

        if valid:
            file = open("passwords.txt", "a")
            file.write(f"website: {website_user_input.get()} | Email/Username: {email_username_input.get()} | Password: {password_input.get()}\n")
            website_user_input.delete(0,'end')
            email_username_input.delete(0,'end')
            password_input.delete(0,'end')
            file.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200,height=200, bg="white",highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1,row=0)

website_label= Label(text="Website:", bg="white")
website_label.grid(column=0,row=1, columnspan=1)

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column=0,row=2,columnspan=1)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0,row=3)

website_user_input = Entry(window,width=35)
website_user_input.grid(row=1,column=1, columnspan=2)
website_user_input.focus()

email_username_input = Entry(window,width=35)
email_username_input.grid(row=2,column=1, columnspan=2 )
email_username_input.insert(0, "Somthing@hotmail.com")

password_input: Entry = Entry(window,width=16)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", bg="white",width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg="white", width=32, height=0, command=add)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()