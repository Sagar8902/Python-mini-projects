from  tkinter import *
from PIL import ImageTk,Image  #import pillow library to insert images

#tk class object
root = Tk()

#add title
root.title("login page")

# icon insert
root.iconbitmap("download.png")

#page minimun size
#root.minsize(400,400)

#particular size's window open
root.geometry("350x500")

#background color
root.configure(background="#0096DC")

#add image
img = Image.open("download.png")
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady = (10,10))

#add flipkart name
text_label = Label(root,text = "Flipkart",fg = "white",bg="#0096DC")
text_label.pack()
text_label.config(font=("vardana",24))

#show email name
email_label = Label(root,text="Enter Email id",fg = "white",bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))

#text box for email
email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

#show password name
password_label = Label(root,text="Enter password",fg = "white",bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",12))

#text box for password
password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

#add login button
login_btn = Button(root,text="login here",bg="white",fg="black",width=18,height=2)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))


root.mainloop()
