from script_for_app.utils import openConnection, closeConnection, clear, bcolors

# QUERY: restituzione tutte le serie tv e i film prodotti in US che hanno un imdb_score>=7.0 e tmdb_score>=8

def menuItem15(ctrl):
    if ctrl == True:
        print(bcolors.OKGREEN + "15 - restituzione di serie tv e film prodotti in US con imdb_score>=7.0 e tmdb_score>=8.0" + bcolors.RESET)
    else:
        print("15 - restituzione di serie tv e film prodotti in US con imdb_score>=7.0 e tmdb_score>=8.0")

def query15():
    clear()
    menuItem15(True)

    db = openConnection()

    resultMovies = db.movies.find({'production_countries': {"$regex": '[^.]?US[^.]?'},'imdb_score': {"$gte":7.0},'tmdb_score': {"$gte":8.0}},{"_id": 0, "title": 1, "imdb_score": 1, "tmdb_score": 1})
    resultShows = db.shows.find({'production_countries': {"$regex": '[^.]?US[^.]?'},'imdb_score': {"$gte":7.0},'tmdb_score': {"$gte":8.0}},{"_id": 0, "title": 1, "imdb_score": 1, "tmdb_score": 1})

    if len(list(resultMovies.clone())) == 0:
        print(bcolors.FAIL + "Non sono presenti nel DB film che soddisfano le condizioni date" + bcolors.RESET)
    else:
        print("************* FILMS *************")
        for doc in resultMovies:
            print('{0} (imdb_score: {1} e tmdb_score:{2})'.format(doc['title'],doc['imdb_score'],doc['tmdb_score']))

    if len(list(resultShows.clone())) == 0:
        print(bcolors.FAIL + "Non sono presenti nel DB serie tv che soddisfano le condizioni date" + bcolors.RESET)
    else:
        print("\n************* SHOWS *************")
        for doc in resultShows:
            print('{0} (imdb_score: {1} e tmdb_score:{2})'.format(doc['title'], doc['imdb_score'], doc['tmdb_score']))

    closeConnection()
    return


