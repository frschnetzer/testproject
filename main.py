import tkinter as tk


master = tk.Tk()
full_name_label = tk.Label(master, text="")

tk.Label(master, text="Full Name Generator", font=("Arial", 20)).grid(row=0, columnspan=3)


tk.Label(master, text='First Name:', font=("Arial", 12), bg="white", fg="black").grid(row=1, column=0, padx=20, pady=20)
tk.Label(master, text='Last Name:', font=("Arial", 12), bg="white", fg="black").grid(row=2, column=0, padx=20, pady=20)

first_name_entry = tk.Entry(master)
last_name_entry = tk.Entry(master)

first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=2, column=1)


def remove_label_text():
    full_name_label.config(text="")


def button_click():
    if len(first_name_entry.get()) != 0 and len(last_name_entry.get()) != 0:
        remove_label_text()
        full_name_label.config(text=f"{first_name_entry.get()} {last_name_entry.get()}", font=("Helvetica", 18))
        full_name_label.grid(row=4, column=1)


submitButton = tk.Button(master, text="Submit", command=button_click, bg="white",fg="black")
submitButton.grid(row=3, column=1)


if __name__ == "__main__":
    master.configure(background="white")
    master.title("Button with event")
    master.geometry("350x350")
    tk.mainloop()
