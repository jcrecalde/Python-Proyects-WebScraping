"""The 100 best songs of the day you were born"""   
"""complete with your details: client id, secret id y name your spoty """
from bs4 import BeautifulSoup 
import requests 
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

DATE = input("Which year do you want to travel to? Type the date, format:YYYY-MM-DD: ") 

URL_PAG = "https://www.billboard.com/charts/hot-100/" 
 
res_pag = requests.get(URL_PAG + DATE) 

soup = BeautifulSoup(res_pag.text, "html.parser") 
all_song = soup.select("li ul li h3") 
 
title_song = [song.getText() for song in all_song]   

spoty_data = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="client id",
        client_secret="secret id",
        show_dialog=True,
        cache_path="token.txt",
        username="spotify name", 
    )
) 
user_id = spoty_data.current_user(["id"]) 

song_uris = [] 
year = DATE.split("-")[0]
for song in all_song: 
    result = spoty_data.search(q=f"track:{song}, year:{year}", type="track") 
    print(result) 
    try: 
        uri = result["tracks"]["items"][0]["uri"] 
        song_uris.append(uri) 
    except IndexError: 
        print(f"{song} song not exist") 
 
playlist = spoty_data.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
spoty_data.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


