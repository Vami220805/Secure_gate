import requests
import datetime

winData = dict()
winData["gateStatus"]= "opened"
winData["lastTimeChanged"]= str(datetime.datetime.now())[2:]
historyData = dict()
historyData["oldStatus"]= "old"
historyData["newStatus"]= "opened"
historyData["lastTimeChanged"]= str(datetime.datetime.now())[2:]

requests.post(url = "https://michael2222.pythonanywhere.com/status" , json = winData)
requests.post(url = "https://michael2222.pythonanywhere.com/history" , json = historyData)

