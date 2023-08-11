import requests

# 输入城市名称
city = input("请输入城市名称：")

# 设置API密钥和API地址
api_key = "YOUR_API_KEY"
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# 发送API请求
response = requests.get(api_url)
data = response.json()

# 提取天气信息
weather = data["weather"][0]["main"]
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]

# 打印天气信息
print(f"城市：{city}")
print(f"天气：{weather}")
print(f"温度：{temperature}K")
print(f"湿度：{humidity}%")

# 注意，该程序仅为示例程序，还需自行填写api地址及api key
