import requests

api_key = 'fab90c15beeeb80422879d7358651875'  # Thay YOUR_API_KEY bằng khóa API của bạn
city = 'Thai Nguyen'
base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)

response = requests.get(base_url)
weather_data = response.json()

if weather_data['cod'] == 200:
    print(f"Thời tiết tại {city}:")
    print(f"Nhiệt độ hiện tại: {weather_data['main']['temp']}°C")
    print(f"Tình trạng thời tiết: {weather_data['weather'][0]['description']}")
else:
    print("Không tìm thấy thông tin thời tiết cho thành phố này.")
