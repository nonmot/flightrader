
import requests
import csv

# データ元のURL
url = 'http://data.flightradar24.com/zones/fcgi/feed.js?bounds=35.6,34.2,131.55,133.55&adsb=1&mlat=1&faa=1&flarm=1&estimated=1&air=1&gnd=1&vehicles=1&gliders=1&array=1'

# リクエストヘッダー
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "accept": "application/json",
    "accept-language": "en-EN",
    "cache-control": "max-age=0",
    "origin": "https://www.flightradar24.com",
    "referer": "https://www.flightradar24.com/"
}

response = requests.get(url, headers=headers)
data = response.json()

data_arr = data['aircraft'][0]
print(data_arr)

with open('flightrader24.csv', 'w') as file:
    fieldname = ['data']
    writer = csv.DictWriter(file, fieldnames=fieldname)
    for i in range(len(data_arr)):
        writer.writerow({'data': data_arr[i]})