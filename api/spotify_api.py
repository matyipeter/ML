import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


client_id = "73414a0f72294f98a0de7edc95f87376"
client_secret = "e31085cdb8b247f2a62607d53041f088"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

music = sp.search(q="Let%20her%20go", type='track', limit=10)

with open('files/lethergo.json', 'w') as output:
    json.dump(music, output, indent=3)
    



