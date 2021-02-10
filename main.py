from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)


    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_file():
    website = url_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Blank Field", message="Don't leave fields blank!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            url_entry.delete(0, END)


def find_password():
    website = url_entry.get()
    if website == "":
        messagebox.showerror(title="Blank Field", message="Don't leave fields blank!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            current_email = data[website]["email"]
            current_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {current_email} \n password: {current_password}")
        except KeyError:
            messagebox.showerror(title="Website Not Found", message="No record of this password")
        except FileNotFoundError:
            messagebox.showerror(title="File Missing", message="No Data File Found")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

url_label = Label(text="Website:")
url_label.grid(row=1, column=0)

website = StringVar()
url_entry = Entry(width=21, textvariable=website)
url_entry.grid(row=1, column=1)
url_entry.focus()

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

email = StringVar()
user_entry = Entry(width=35, textvariable=email)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "jason.d.guest@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password = StringVar()
password_entry = Entry(width=21, textvariable=password)
password_entry.grid(row=3, column=1)


password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)





add_button = Button(text="Add", width=36, command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
