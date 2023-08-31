import requests

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}".format(city=city, API_KEY="YOUR_API_KEY")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data

def main():
    city = input("Enter a city name: ")
    weather = get_weather(city)

    print("The weather for {}:".format(city))
    print("Currently: {}".format(weather["weather"][0]["main"]))
    print("Highest temperature: {}".format(weather["main"]["temp_max"]))
    print("Lowest temperature: {}".format(weather["main"]["temp_min"]))

if __name__ == "__main__":
    main()
