# 2018/6/18
# ng

import os, re, glob, pathlib, shutil, time, datetime, requests
from pathlib import Path

url = "http://weather.livedoor.com/forecast/webservice/json/v1"
payload = { "city": "130010"}
wearher_data = requests.get(url, paramas=payload).json()

for wearher in wearher_data["forecast"]:
	print(
		wearher["datelabel"]
		+ "の天気は"
		+ wearher["telop"]
		)
		



