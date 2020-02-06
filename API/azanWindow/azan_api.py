import json
import requests

class azanApi():
    def __init__(self, zone):

        api_call ='http://api.azanpro.com/times/today.json?zone=' +zone+ '&format=12-hour'
        self.conn = requests.get(api_call)
        self.zones = requests.get('http://api.azanpro.com/zone/zones.json?')
        self.hook = self.conn.json()
        print(self.hook)

    def solatTime(self, waktu='subuh'):
        imsak = self.hook['prayer_times']['imsak']
        subuh = self.hook['prayer_times']['subuh']
        syuruk = self.hook['prayer_times']['syuruk']
        zohor = self.hook['prayer_times']['zohor']
        asar = self.hook['prayer_times']['asar']
        maghrib = self.hook['prayer_times']['maghrib']
        isyak = self.hook['prayer_times']['isyak']
        self.azan_time = {"imsak":imsak, 'subuh':subuh, 'syuruk':syuruk, 'zuhur':zohor, 'asar':asar, 'maghrib':maghrib, 'isyak':isyak}
        return self.azan_time[waktu]











