import requests
import datetime

winData = dict()
winData["gateStatus"]= "opened"
winData["lastTimeChanged"]= str(datetime.datetime.now())[2:]

requests.post(url = "https://michael2222.pythonanywhere.com/status" , json = winData)
