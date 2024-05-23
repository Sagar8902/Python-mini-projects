import io
import webbrowser
import requests
from  tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
class NewsApp:

    def __init__(self):

        #fetch data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=c17af33e0188485bac7cc6f6de54ddee").json()
        print(self.data)

        #initial GUI load
        self.load_gui()

        #load the 1st news
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.title("Apna News")
        self.root.configure(background="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        #clear the screen for the new news item
        self.clear()

        #add image
        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
        except:
            img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8DtCukkfEK5gzGzKan9gtedpqb1tWHdBj5Q&s"
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(img)


        label = Label(self.root,image=photo)
        label.pack()

        #add heading
        heading = Label(self.root,text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=350,justify="center")
        heading.pack(pady=(10,20))
        heading.config(font=("verdana",12))

        # add news detail
        details = Label(self.root, text=self.data["articles"][index]["description"], bg="black", fg="white", wraplength=350,justify="center")
        details.pack(pady=(10, 20))
        details.config(font=("verdana", 10))


        frame = Frame(self.root,bg="black")
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text="Prev",width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text="Read More", width=16, height=3,command=lambda :self.open_link(self.data["articles"][index]["url"]))
        read.pack(side=LEFT)

        if index != len(self.data["articles"])-1:
            next = Button(frame, text="Next", width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()
