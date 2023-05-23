# Weather App using Weather Api
import requests

def data_get():
   print("\t\tWelcome to the Weather Forecaster!\n")
   print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n\n")
   city= input("Enter the name of the City : ")
   print("\n\n")
   try:
      data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=41c3d7306bb80b0bfc1c823e04e2f078").json()

      # Printing Weather Details
      print(f"Weather :",data["weather"][0]["main"])
      print(f"Weather Description:",data["weather"][0]["description"])
      print(f"Temprature :",int(data["main"]["temp"]-273.15))
      print(f"Pressure :",data["main"]["pressure"])
      print(f"Minimum Temprature :",int(data["main"]["temp_min"]-273.15))
      print(f"Maximum Temprature :",int(data["main"]["temp_max"]-273.15))
      print(f"Humidity :",data["main"]["humidity"])
      print(f"Wind Speed:",data["wind"]["speed"])

   # Handle Error
   except Exception as e :
      print("Some Exception Occured:",e)

data_get()

