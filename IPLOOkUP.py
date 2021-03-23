import os
import urllib.request
import json
from urllib import *
from platform import system
import sys
from datetime import datetime
import time


def slowprint(s):

    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)


def ipinfo():
       ip=input(" Enter IP Address : \033[1;32m ")
       url = ("http://ip-api.com/json/")
       response = urllib.request.urlopen(url + ip)
       data = response.read()
       values = json.loads(data)
       os.system("clear")

print ("\033[1;32m\007\n")
       os.system("figlet IP-Info | lolcat")
       slowprint("\033[1;33m|            IP Information           |")
       slowprint("\033[1;36m" + "\n IP          : \033[1;32m " + values['query'])
       slowprint("\033[1;36m" + " Status      : \033[1;32m " + values['status'])
       slowprint("\033[1;36m" + " Region      : \033[1;32m " + values['regionName'])
       slowprint("\033[1;36m" + " Country     : \033[1;32m " + values['country'])
       slowprint("\033[1;36m" + " Date & Time : \033[1;32m " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       slowprint("\033[1;36m" + " City        : \033[1;32m " + values['city'])
       slowprint("\033[1;36m" + " ISP         : \033[1;32m " + values['isp'])
       slowprint("\033[1;36m" + " Lat,Lon     : \033[1;32m " + str(values['lat']) + "," + str(values['lon']))
       slowprint("\033[1;36m" + " ZIPCODE     : \033[1;32m " + values['zip'])
       slowprint("\033[1;36m" + " TimeZone    : \033[1;32m " + values['timezone'])
       slowprint("\033[1;36m" + " AS          : \033[1;32m " + values['as'] + "\n")





       print (" ")
