from movie_model import MovieModel
import requests
from werkzeug.wrappers import response

# router에서 사용하기 위해 함수
def callMoveApi():
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json()
    movies = responseDict["data"]["movies"]

    return convert_model(movies)

def convert_model(movies):
    list=[]
    for movie in movies:
        movie_model = MovieModel(movie["rating"],movie["summary"],
                        movie["small_cover_image"],movie["title"]) 
        list.append(movie_model)
    return list