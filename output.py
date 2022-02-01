# ライブラリのインストール
import requests
import csv

# データ元のURL
url = 'http://data.flightradar24.com/zones/fcgi/feed.js?bounds=&adsb=1&mlat=1&faa=1&flarm=1&estimated=1&air=1&gnd=1&vehicles=1&gliders=1&array=1'

# リクエストヘッダー
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "accept": "application/json",
    "accept-language": "en-EN",
    "cache-control": "max-age=0",
    "origin": "https://www.flightradar24.com",
    "referer": "https://www.flightradar24.com/"
}

# リクエストを送信
response = requests.get(url, headers=headers)

#レスポンスをjsonにがあればjson形式にする
data = response.json()

data_arr = data['aircraft']

# 取得したデータを標準出力
# for i in range(len(data_arr)):
#     print(data_arr[i])


# CSVへの書き込み
# 列名
columns = ['列01', '列02', '列03', '列04', '列05', '列06', '列07', '列08', '列09', '列10',
            '列11', '列12', '列13', '列14', '列15', '列16', '列17', '列18', '列19', ]

with open('flightrader24.csv', 'w', encoding='utf-8_sig') as file:
    fieldname = ['data']
    writer = csv.writer(file)
    writer.writerow(columns)
    for data in data_arr:
        writer.writerow(data)