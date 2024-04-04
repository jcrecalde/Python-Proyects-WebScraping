"""Top 100 best movies"""  
import requests 
from bs4 import BeautifulSoup 

URL_PAG = "https://www.empireonline.com/movies/features/best-movies-2/" 

res_pag = requests.get(URL_PAG) 
website_html = res_pag.text 

soup = BeautifulSoup(website_html, "html.parser") 
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")  
 
titles_movies = [movie.getText() for movie in all_movies] 
movies = titles_movies[::-1] 

with open("top_100_movies.txt", "w") as file:   
    for movie in movies:
        file.write(f"{movie}\n")

