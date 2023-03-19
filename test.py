from urllib.request import urlopen
import json


json_url = urlopen()
data = json.loads(json_url.read())

print(data)
