import json
import requests
maps = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Lawyer%20London%20Ontario&inputtype=textquery&fields=photos,'
                    'formatted_address,name,rating,opening_hours,geometry&key='
                    'AIzaSyBIN-ETogb9Xdf8TYcPL6aBjIogAGc7llQ')
print(maps.json())
