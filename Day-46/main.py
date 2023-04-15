
from bs4 import BeautifulSoup
import requests
import spotipy

import os
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyOAuth


#taking api credentials from .env file
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")
client_id= os.getenv("spotify_id")
client_secret= os.getenv("spotify_secret")

#asking user for date and getting the list of songs from billboard

print("Welcome to the Billboard 100 Songs of the Week Scrapper")
date=input("Enter the date in YYYY-MM-DD format: ")
response= requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
# print(response.status_code)
soup= BeautifulSoup(response.text,"html.parser")
list= soup.select("li ul li h3")
# print(list)

#create a list of songs
songs=[song.getText().strip() for song in list]
# print(songs)


# #searching for the songs in spotify and getting the uri of the songs without spotipy
#made me realize how godlike spotipy is


#getting the token so that i can use the api (kind of useless thing to do imo)

# def get_token():
#     auth_string= f"{client_id}:{client_secret}"
#     auth_bytes= auth_string.encode("utf-8")
#     auth_base64= base64.b64encode(auth_bytes)
    
#     url="https://accounts.spotify.com/api/token"
    
#     headers={
#         "Authorization": f"Basic {auth_base64.decode('utf-8')}",
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
    
#     data={"grant_type": "client_credentials"}
    
#     result= requests.post(url=url,headers=headers,data=data)
#     json_result=json.loads(result.content)
#     token=json_result["access_token"]
#     return token

#using the token from above and creating a function to get the auth header

# def get_auth_header(token):
#     return {"Authorization": f"Bearer {token}"}


#creating a function to search for the song and get the uri of the song and cwd to the uri list

# uri=[]
# def search_song(song):
#     url = "https://api.spotify.com/v1/search"
#     header= get_auth_header(token)
#     query= f"q={song}&type=track"
#     query_url= f"{url}?{query}"
#     response= requests.get(url=query_url,headers=header)
#     json_result= json.loads(response.content)
#     # print(song)
#     uri.append(json_result['tracks']['items'][0]['uri'])
# token=get_token()
# for song in songs:
#     search_song(song)

#here comes the spotipy . it is so much easier to use than the above code


#we are using the scope playlist-modify-private because we are creating a private playlist
#we are using the redirect_uri as localhost because we are using the terminal to run the code
#we are using the cache_path as token.txt so that we dont have to login everytime we run the code
#we are using the show_dialog as True so that we can see the login page everytime we run the code
#we are using the client_id and client_secret from the .env file to get the credentials and we don't need to get the token and auth header
#we are using the user_id to get the user id of the user who is logged in
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=client_id,
        client_secret= client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

song_uris = []
year = date.split("-")[0]

#searching for the song in spotify and getting the uri of the song and appending it to the uri list if it exists.
#so much easier now that we are using spotipy
#i love spotipy developers. they are so godlike
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
#creating a playlist and adding the songs to the playlist
playlist_name= input("Enter the name of the playlist: ")
user_id= sp.current_user()["id"]
print(user_id)
playlist= sp.user_playlist_create(user=user_id,name=playlist_name,public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)