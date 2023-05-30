
from tkinter import *
import requests
from tkinter import messagebox
from WeatherApp import WeatherApp

def GetWeather():
    start = WeatherApp.Startweather()
    return start



class NewsApp():
    def __init__(self,app):
        self.app = app
        self.app.title("NewsApp")
        self.app.geometry("1470x600")

    # Variable
        self.NewsCatButton = []
        self.NewsCat = ["General","Entertainment","Business","Health","Science","Technology"]

    # GUI
        blue = '#081D54'
        light_blue = '#0066cc'
        font_color = 'white'
        self.title = Label(self.app,text= "NEWSAPP",font=("rockkwell bold",30),bg=blue,fg=font_color,relief='raised',pady=5,bd=10).pack(fill=X)

        f1 = LabelFrame(self.app,text="Categories",bg=blue,fg=font_color,font=('roboto slab',20,'bold'),bd=10,relief="raised")
        f1.place(x=0,y=80,width =300,relheight=0.88)

        for i in range(len(self.NewsCat)):
            b = Button(f1,text=self.NewsCat[i].upper(),fg=font_color,font=('roboto slab',14,'italic'),relief='flat',bg=light_blue,bd=7,width=20,height=2)
            b.grid(row=i,column=0,padx=20,pady=6)
            b.bind('<Button-1>',self.NewsArea)
            self.NewsCatButton.append(b)

        f2 = Frame(self.app,bg='white',relief='groove',bd=1)
        f2.place(x=310,y=80,relheight=0.88,relwidth=0.79)
        newsTitle = Label(f2,text="NEWS AREA",bg=light_blue,fg='white',font=("rockkwell bold",20),relief='groove')
        newsTitle.pack(fill=X)

        Scroll_y = Scrollbar(f2,orient=VERTICAL)
        self.textarea = Text(f2,yscrollcommand=Scroll_y.set,font=('lora bold',15),bg = light_blue,fg=font_color)        
        Scroll_y.pack(fill=Y,side=RIGHT)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.insert(END,"\n\t\n\t\n\t\n\t\n\t\t\t\n\n\n\t\t\t\tPLEASE SELECT THE CATEGORY TO SEE HEADLINES\n\t\t\tPLEASE BE PATIENT, IT DEPENDS UPON YOUR INTERNET CONNECTION")
        self.textarea.pack(fill=X)

        self.b2 =Button(f2,text='Weather Mate'.upper(),font=("rockwell",16),bg = 'yellow',fg = blue,width=20,bd=7,command=GetWeather)
        self.b2.place(x=0,y=625,relwidth=1,relheight=0.1)

    
    def NewsArea(self,event):
        type = 'general'
        type = event.widget.cget("text").lower()
        apiKey = "<YOUR_NEWS_API_KEY>"        
        Baseurl = f'https://newsapi.org/v2/top-headlines?country=us&category={type}&apiKey={apikey}'
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,'READ THE NEWS PROVIDED BY OUR NEWSAPP!!!')
        self.textarea.insert(END,'---------------------------------------------------------------------------------------------\n\n')
        try:
            articles = (requests.get(Baseurl).json())['articles']
            if (articles!=0):
                for i in range(len(articles)):
                    self.textarea.insert(END,f"{articles[i]['title']}\n")
                    self.textarea.insert(END,f"{articles[i]['description']}\n\n")
                    self.textarea.insert(END,f"{articles[i]['content']}\n\n")
                    self.textarea.insert(END,f"readmore......{articles[i]['url']}\n")
                    self.textarea.insert(END,"\n--------------------------------------------------------------------------\n")
                    self.textarea.insert(END,"--------------------------------------------------------------------------\n\n")
            else:
                self.textarea.insert(END,"SORRY NO NEWS AVAILABLE")
        except Exception as e:
            messagebox.showerror("ERROR!, Sorry cannot connect to internet or some issue within the newsapp :(")
           



app = Tk()  
NewsApp(app)
app.state("zoomed")

app.mainloop()