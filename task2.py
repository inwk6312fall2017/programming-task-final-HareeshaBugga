import datetime
import json
import urllib.request


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = 'http://openweathermap.org/city/6324729' 
    unit = 'metric'  
    api = 'http://api.openweathermap.org/data/2.5/weather?id=6324729'    

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url

def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict
if __name__ == '__main__':
    try:
        data_output(data_organizer(data_fetch(url_builder(2172797))))
    except IOError:
        print('no internet')
