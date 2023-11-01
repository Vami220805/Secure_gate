import requests
import datetime

winData = dict()
winData["gateStatus"]= "closed"
winData["lastTimeChanged"]= str(datetime.datetime.now())[2:]
historyData = dict()
historyData["oldStatus"]= "old"
historyData["newStatus"]= "closed"
historyData["lastTimeChanged"]= str(datetime.datetime.now())[2:]

requests.post(url = "https://michael2222.pythonanywhere.com/status" , json = winData)
requests.post(url = "https://michael2222.pythonanywhere.com/history" , json = historyData)

