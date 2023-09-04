import requests
api='8482add37b86f163232406cfc0f04a82'#from weather org
#install requests module type pip3 install requests
city=input('enter city :')
print (city)
weather_report=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}")

#print(weather_report.status_code)#if 200 then api works if 404 
if weather_report.json()['cod']=='404':
    print(f"{city} not found")
else:
    w=weather_report.json()['weather'][0]['main']
    temp=weather_report.json()['main']['temp']
    feel_like=weather_report.json()['main']['feels_like']
    humidity=weather_report.json()['main']['pressure']
    visibility=weather_report.json()['visibility']
    wind=weather_report.json()['wind']
    clouds=weather_report.json()['clouds']
    print('Weather : ',w)
    print("Temperature : ",temp, "ºF")
    print("Feels like ",feel_like)
    print("Humidity : ",humidity)
    print("Visibility : ",visibility)
    print("wind speed and angle ",wind)
    print("status of clouds" ,clouds)

