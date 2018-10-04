"""
Client ID

RcAMzRQvgL0P9wWr-goS5w
API Key

s8vSxwznFf6rfI-R5Tbp_rv1fTf4iaBXLtirzcm1zQZMHdCagjU18uhCO1YR5UPwgXr67joptzMZ9nGbCmoBd3j2so1X2IOW4FTtGS7UbV2umbw04vgQDbcL6WG2W3Yx

"""
import requests
import pprint
import json

search_string = 'https://api.yelp.com/v3/businesses/search?term=delis&latitude=37.786882&longitude=-122.399972'
api_key = 'Bearer s8vSxwznFf6rfI-R5Tbp_rv1fTf4iaBXLtirzcm1zQZMHdCagjU18uhCO1YR5UPwgXr67joptzMZ9nGbCmoBd3j2so1X2IOW4FTtGS7UbV2umbw04vgQDbcL6WG2W3Yx'

r = requests.get("https://api.yelp.com/v3/businesses/search?location=NYC", headers={"content-type": "text", "Authorization": api_key})

jsn = r.json()

pp = pprint.PrettyPrinter()
pp.pprint(jsn)
