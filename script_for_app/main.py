from time import sleep
from script_for_app.utils import clear, bcolors
from script_for_app.query_1 import query1, menuItem1
from script_for_app.query_2 import query2, menuItem2
from script_for_app.query_3 import query3, menuItem3
from script_for_app.query_4 import query4, menuItem4
from script_for_app.query_5 import query5, menuItem5
from script_for_app.query_6 import query6, menuItem6
from script_for_app.query_7 import query7, menuItem7
from script_for_app.query_8 import query8, menuItem8
from script_for_app.query_9 import query9, menuItem9
from script_for_app.query_10 import query10, menuItem10
from script_for_app.query_11 import query11, menuItem11
from script_for_app.query_12 import query12, menuItem12
from script_for_app.query_13 import query13, menuItem13
from script_for_app.query_14 import query14, menuItem14
from script_for_app.query_15 import query15, menuItem15
from script_for_app.query_16 import query16, menuItem16
from script_for_app.query_17 import query17, menuItem17
from script_for_app.query_18 import query18, menuItem18
from script_for_app.query_19 import query19, menuItem19
from script_for_app.query_20 import query20, menuItem20

def menu():
    print(bcolors.OKGREEN + "---------------- MENU ----------------" + bcolors.RESET)
    print("Seleziona l'operazione sul DB da eseguire digitando il numero associato:")
    menuItem1(False)
    menuItem2(False)
    menuItem3(False)
    menuItem4(False)
    menuItem5(False)
    menuItem6(False)
    menuItem7(False)
    menuItem8(False)
    menuItem9(False)
    menuItem10(False)
    menuItem11(False)
    menuItem12(False)
    menuItem13(False)
    menuItem14(False)
    menuItem15(False)
    menuItem16(False)
    menuItem17(False)
    menuItem18(False)
    menuItem19(False)
    menuItem20(False)

    op = int(input(bcolors.OKGREEN + "Inserisci il numero dell'operazione da eseguire:" + bcolors.RESET))
    return op

ctrl = True #condizione di controllo per l'iterazione del ciclo

while ctrl == True:
    clear()
    op = menu() #visualizzo menu operazioni
    print('Hai selezionato operazione: ' + str(op))

    if (op == 1):
        query1()
    elif (op == 2):
        query2()
    elif (op == 3):
        query3()
    elif (op == 4):
        query4()
    elif (op == 5):
        query5()
    elif (op == 6):
        query6()
    elif (op == 7):
        query7()
    elif (op == 8):
        query8()
    elif (op == 9):
        query9()
    elif (op == 10):
        query10()
    elif (op == 11):
        query11()
    elif (op == 12):
        query12()
    elif (op == 13):
        query13()
    elif (op == 14):
        query14()
    elif (op == 15):
        query15()
    elif (op == 16):
        query16()
    elif (op == 17):
        query17()
    elif (op == 18):
        query18()
    elif (op == 19):
        query19()
    elif (op == 20):
        query20()

    response = input('Vuoi proseguire?: si/no: ')

    if (response == 'no'):
        ctrl = False

print("L'esecuzione terminerà tra 5 secondi...")
sleep(5)
clear()