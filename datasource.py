import requests

sarea_list = None

def getInfo():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    response = requests.get(url)
    data_list = response.json()
    sarea_temp = set ()
    for item in data_list:
        sarea_temp.add(item["sarea"])
        print (item["sarea"])
    sarea_list = list(sarea_temp)

    