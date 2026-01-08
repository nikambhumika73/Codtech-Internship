import requests
import matplotlib.pyplot as plt

API_KEY = "c57338f4554d2e539e0bdfdf6d1ce5cc"
CITY = "Pune"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Check if API call was successful
if "main" in data:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    labels = ["Temperature (°C)", "Humidity (%)"]
    values = [temperature, humidity]

    plt.bar(labels, values)
    plt.title(f"Weather Data for {CITY}")
    plt.show()
else:
    print("API Error:", data)
