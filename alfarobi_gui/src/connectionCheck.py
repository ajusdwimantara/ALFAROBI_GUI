import urllib.request
import json

def internet_on():
    try:
        urllib.request.urlopen('http://142.251.10.139', timeout=2) #using google ip address
        return True
    except urllib.request.URLError as err: 
        return False

# Opening JSON file
with open('/home/ajus/Desktop/alfarobi_ws/src/alfarobi_gui/config/GlobalConfig.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

# print(json_object["feedback"])
is_updated = bool()
internet_status = internet_on()
if(internet_status):
    print("Connected to the internet!")
    is_updated = json_object["is_updated"]
else:
    print("No internet connection!")
    json_object["is_updated"] = True
    is_updated = json_object["is_updated"]


    