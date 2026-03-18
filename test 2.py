from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Student Form")

# Window settings
root.geometry("500x500")
root.configure(bg="#FF2504")

# Icon
if os.path.exists("pixel2.ico"):
    root.iconbitmap("pixel2.ico")

# -------- IMAGE --------
try:
    image = Image.open("star.png")     # make sure star.png is in same folder
    image = image.resize((120, 80))    # resize image
    photo = ImageTk.PhotoImage(image)

    img_label = Label(root, image=photo, bg="#FF2504")
    img_label.pack(pady=15)

except:
    print("Image not found")

title = Label(root,
              text="Giet Bucks",
              font=("Arial", 20, "bold"),
              bg="#FF2504",
              fg="white")
title.pack(pady=10)

email_label = Label(root,
                    text="Email",
                    font=("Arial", 14, "bold"),
                    bg="#FF2504",
                    fg="white")
email_label.pack(pady=(20,5))

email_entry = Entry(root, font=("Arial", 14))
email_entry.pack()

password_label = Label(root,
                       text="Password",
                       font=("Arial", 14, "bold"),
                       bg="#FF2504",
                       fg="white")
password_label.pack(pady=(20,5))

password_entry = Entry(root, font=("Arial", 14), show="*")
password_entry.pack()

login_btn = Button(root,
                   text="Login",
                   font=("Arial", 14, "bold"),
                   bg="white",
                   fg="black",
                   width=12)
login_btn.pack(pady=30)

root.mainloop()
