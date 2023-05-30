from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import requests



class WeatherApp:
    global url,apiKey
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    
    apiKey = "<YOUR_WEATHER_API_KEY>"
    def __init__(self,root):
        self.root = root
        self.root.title("Weather Mate")
        self.root.geometry('380x450+550+150')
        self.root['bg']='pink'
        # self.txt = Label(text = "Weather Mate- by Vishwa Panchal",font = ("rockwell bold",16),bg = 'green',fg = 'yellow')
        # self.txt.pack(pady = 20)
        
        cityText = StringVar()
        cityEntry = ttk.Entry(root,text = cityText,font=('arial bold',30),style = 'Entrystyle.TEntry',justify='center',width=20)
        cityEntry.pack(pady = 0)
        cityEntry.focus()
        blue = '#0066CC'

        def CheckWeather(city):
            result = requests.get(url.format(city,apiKey))
            if result:
                json = result.json()
                city = json['name']#0
                country = json['sys']['country']#1
                temp_kelvin = json['main']['temp']#
                temp_celcius = temp_kelvin - 273.15#2
                temp_farenheit = temp_celcius*(9/5)+32#3
                icon = json['weather'][0]['icon']#4
                final = (city,country,temp_celcius,temp_farenheit,temp_kelvin,icon)
                return final
            else:
                return None

        def searchedfor(app):
            city = cityText.get()
            weather = CheckWeather(city)
            if weather:
                location['text']=f'{weather[0]}, {weather[1]}'
                temperature['text']=f'{weather[2]:.2f} Celcius,{weather[3]:.2f} Farenheit,'
                intro.destroy() 
            else:
                messagebox.showerror(f"Error!,COuld not find the city name!{city} :(")
            print(f"Search for city {city}")


        def press():
            intro.destroy()
            searchedfor(root)

        search = Button(root,text="Get Weather", font=("rockwell bold",16),width=20,height=4,bg=blue,fg='white',command=press)
        search.pack(pady=50)
        
        cityEntry.bind('<Return>',searchedfor)

        location = Label(root,text='',bg='pink',fg='black',font=('rockwell bold',16))
        location.pack()

        intro = Label(root,text="Search by - City/State/Country",font=('rockwell bold',15),bg='pink',fg='red',width=40,height=5)
        intro.pack(pady=20)

        temperature = Label(root,text='',font=('rockwell bold',16),bg='pink',fg='black')
        temperature.pack()


    def Startweather():   
        root = Toplevel()
        WeatherApp(root)
        root.mainloop()