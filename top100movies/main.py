import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html = BeautifulSoup(response.text, "html.parser")
titles = html.select("h3[class]")
movies = [n.getText() for n in titles]
movies.reverse()
with open("movies_to_watch.txt","w") as file:
    for movie in movies:
        file.write(movie+"\n")
print(movies)
