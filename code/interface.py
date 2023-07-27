"""
API waarmee de webInterface kan comuniceren met python code.
"""

# importeer nodioge modules en defineer alle basis variabelen
import webview
import os
import subprocess
import requests
import time

URL = "https://michael2222.pythonanywhere.com/status"

# maak in de functie startWebInterface de class Api aan, deze kan gebruikt worden in de javascript van de webInterface
# dit wordt in een functie gedaan zodat we deze in een afzonderlijke thread kunnen uitvoeren
# de class Api heeft de volgende functies:
## exit: stuurt commando naar de server om spel stop te zetten, zet "exit" in de queue en sluit na 1 seconde het progamma af
## start: stuurt commando naar de server om spel te starten en zet "start|--doorgegeven player data--" in de queue
## color: zet "color|--doorgegeven kleur data--" in de queue
## stop: stuurt commando naar de server om spel stop te zetten en zet "stop" in de queue
# door een bug is minstens 1 parameter nodig, bij functies zonder parameters wordt een lege string doorgegeven om een error te voorkomen
def startWebInterface(queue):
    class Api:
        def __init__(self):
            pass
        
        def passThrough(self, gate):
            queue.put(gate)

    api = Api()