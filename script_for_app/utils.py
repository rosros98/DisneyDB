from pymongo import MongoClient
import os

client = None

def clear():
    if (os.name == 'posix'):
        os.system("clear")
    else:
        os.system("cls")

def openConnection():
    global client
    client = MongoClient("mongodb://localhost:27017")   # apro connessione con mongoDB
    print(bcolors.OKYELLOW + "Connection successfully activated\n" + bcolors.RESET)
    db = client["disneyDB"]

    return db

def closeConnection():
    global client
    client.close()      # chiudo connessione con mongoDB
    print(bcolors.OKYELLOW + "Connection successfully disactivated\n" + bcolors.RESET)


class bcolors:
    HEADER = '\033[95m' #fucsia
    OKBLUE = '\033[94m' #azzurro
    OKCYAN = '\033[96m' #tiffany
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m' #giallo
    FAIL = '\033[91m' #rosso
    BOLD = '\033[1m' #grassetto
    UNDERLINE = '\033[4m' #sottolineato
    RESET = '\033[0m' #RESET COLOR