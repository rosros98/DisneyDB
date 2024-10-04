from script_for_app.utils import openConnection, closeConnection, clear, bcolors

#QUERY : aggiornamento di score e numero stagioni di una determinata serie

def menuItem5(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "5  - update di imdb_score da 5.8 a 7.0 e numero stagioni da 1 a 3 della serie tv \'Spider-Woman\'" + bcolors.RESET)
    else:
        print("5  - update di imdb_score da 5.8 a 7.0 e numero stagioni da 1 a 3 della serie tv \'Spider-Woman\'")

def query5():
    clear()
    menuItem5(True)

    db = openConnection()

    result = db.shows.find({"id": "ts24939"}, {'_id':0, 'id':0,'imdb_id': 0,'imdb_votes': 0,'tmdb_popularity': 0,'tmdb_score': 0})
    print(bcolors.OKGREEN + "\nRecupero dati serie..." + bcolors.RESET)
    for doc in result:
        print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: {4} - paesi di produzione: {5}\nstagioni: {6} per episodi di {7} minuti\nimdb_score: {8}'.format(doc['title'],doc['release_year'],doc['description'],doc['genres'],doc['age_certification'],doc['production_countries'],doc['seasons'],doc['runtime'],doc['imdb_score']))

    #Miglioramento di score da 5.8 a 7.0 e quindi all'unica stagione se ne aggiungono altre due
    update = db.shows.update_one({"id": "ts24939"}, {"$set": {"imdb_score": 7.0, "seasons": 3}})

    result2 = db.shows.find({"id": "ts24939"},{'_id': 0, 'id': 0, 'imdb_id': 0, 'imdb_votes': 0, 'tmdb_popularity': 0,'tmdb_score': 0})
    print(bcolors.OKGREEN + "\nRecupero dati serie aggiornati..." + bcolors.RESET)
    for doc in result2:
        print('title: {0} ({1})\ndescription: {2}\ngenere: {3} - certificazione età: {4} - paesi di produzione: {5}\nstagioni: {6} per episodi di {7} minuti\nimdb_score: {8}'.format(doc['title'], doc['release_year'], doc['description'], doc['genres'], doc['age_certification'],doc['production_countries'], doc['seasons'], doc['runtime'], doc['imdb_score']))

    print("aggiornamento avvenuto con successo")

    closeConnection()
    return