import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

pp = pprint.PrettyPrinter(indent=2)

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'las vegas'
r = requests.get(API_URL + city)
response = r.json()


pp.print(response)
forecast_list = response['forecast']

today = datetime.now().strftime("%b-%d-%Y")

to_graph = {}
count = 1
for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count += 1 if current_date <= 31 else 1

day['wind'] = 0 if day['wind'][0] == ' ' else int(day['wind'][:2])

to_graph[this_day] = day['wind']

plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')

plt.scatter(to_graph.keys(), to_graph.values())
plt.show()

