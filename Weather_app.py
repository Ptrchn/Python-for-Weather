import tkinter as tk
import requests
import time

def getWeather(UI):
    city = Box.get()
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=-------your api---------'


    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 25200))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 25200))

    final_info = condition + '\n' + str(temp) + '°C'
    final_data = '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min Temp: ' + str(min_temp) + '\n' + 'Pressure: ' + str(pressure) + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Wind Speed: ' + str(wind) + '\n' + 'Sunrise: ' + sunrise +'\n' + 'Sunset: ' + sunset\
    
    L1.config(text = final_info)
    L2.config(text = final_data)
    


UI = tk.Tk()
UI.geometry('600x500')
UI.title('Weather App')

FONT1 = ('Angsana New' , 15)
FONT2 = ('Angsana New' , 35)

Box = tk.Entry(UI, font = FONT1)
Box.pack(pady = 20)
Box.focus()
Box.bind('<Return>', getWeather)

L1 = tk.Label(UI, font = FONT2)
L1.pack()
L2 = tk.Label(UI, font = FONT1)
L2.pack()

UI.mainloop()