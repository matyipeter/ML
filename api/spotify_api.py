import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import random

# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# music = sp.search(q="Let%20her%20go", type='track', limit=10)

# with open('files/lethergo.json', 'w') as output:
#     json.dump(music, output, indent=3)
    
# print(music['tracks']['items'][0])


# preparations
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# user input
artist = input('Who is your favourite artist? ')

# get the name of the albums
def get_albums(artist):
    albums = sp.search(q=f'artist:{artist}',type='album', limit=30)
    albums = albums['albums']['items']
    album_names = [i['name'] for i in albums]
    return album_names

albums = get_albums(artist)
choice = random.choice(albums).split()

#print(choice)
max_len = choice[0]
for i in choice:
    if len(i) > len(max_len):
        max_len = i

def create_guess_word(max_len):
    guess_word = []
    for _ in range(len(max_len)):
        guess_word.append('_')
    return guess_word

def guess_assess(guess_word, guess, max_len):
    if guess == max_len:
        print('Kitaláltad!')
        return True
    else:
        for index,item in enumerate(max_len):
            try:
                if item == guess[index]:
                    guess_word[index] = item
            except:
                print('he')
        print("".join(guess_word))
    
guess_word = create_guess_word(max_len)
while True:
    guess = input('Take a guess: ')
    if guess_assess(guess_word, guess, max_len):
        break
    








