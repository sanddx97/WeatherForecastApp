import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key

def get_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather():
    location = location_entry.get()
    weather_data = get_weather_data(location)
    
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        weather_info = (f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s\n"
                        f"Description: {description}")

        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Unable to fetch weather data for the given location")

def save_favorite():
    location = location_entry.get()
    with open('favorites.txt', 'a') as file:
        file.write(location + '\n')
    messagebox.showinfo("Saved", "Location saved to favorites")

app = tk.Tk()
app.title("Weather Forecast App")

tk.Label(app, text="Enter Location:").pack()
location_entry = tk.Entry(app)
location_entry.pack()

tk.Button(app, text="Get Weather", command=display_weather).pack()
tk.Button(app, text="Save to Favorites", command=save_favorite).pack()

weather_label = tk.Label(app, text="", justify="left")
weather_label.pack()

app.mainloop()
