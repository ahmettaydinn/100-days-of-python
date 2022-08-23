from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import spotipy

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')

song_names_spans = soup.select(selector='.o-chart-results-list__item .c-title')
song_names = [song.getText() for song in song_names_spans]
song_names_stripped = []
for i in song_names:
    song_names_stripped.append(i.strip('\t\n'))

CLIENT_ID = "YOUR CLIENT ID IN SPOTIFY"
CLIENT_SECRET = "YOUR CLIENT SECRET IN SPOTIFY"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR CLIENT ID IN SPOTIFY",
        client_secret="YOUR CLIENT SECRET IN SPOTIFY",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names_stripped:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
