#imports
import requests
import json
import time

# Read in secret key from json file
try:
    secret_key_file  = open("../spotify/secret/secret_key.json")
    secret_key_json = json.load(secret_key_file)
    secret_key = secret_key_json.get("secret_key")
    secret_key_file.close()
except:
    try:
        with open('../secret/secret_key.json') as secret_key_file:
            secret_key_json = json.load(secret_key_file)
            secret_key = secret_key_json.get('secret_key')
    except: 
        print('something went wrong looking for secret key')

#create the get_token function to ask spotify api for an access token
def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {secret_key}",
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type" : "client_credentials"
    }
    response = requests.post(url, data = data, headers = headers)
    
    return response.json()


def get_available_genre_seeds():
    #define base url
    url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"

    #get token to put in headers
    access_token = get_token().get("access_token")
    
    #define headers
    headers = {
        "Authorization" : f"Bearer {access_token}" ,
        "Content-Type" : "application/json"
    }

    #ask spotify for data
    response = requests.get(url, headers = headers)

    #return data
    return response.json()
    
# def save_genres():
#     #get genre seeds from spotify
#     genre_seeds = get_available_genre_seeds().get("genres")

#     #write seeds to file
#     with open("../spotify/data/genre_seeds.txt", "w") as fp:
#         for item in genre_seeds:
#             fp.write("%s\n" % item)
#         print("Done")


# def read_genres():
#     with open("../spotify/data/genre_seeds.txt", "r") as fp:
#         genres = [line[:-1] for line in fp]
#     print("Done")
    
#     return genres 
# genre_seeds = read_genres()


def recommendations(track_id = "4nFAL2TKUOoAPQJ5DGGoTd"):
   # url = "https://api.spotify.com/v1/recommendations?seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_genres=classical,country&seed_tracks=0c6xIDDpzE81m2q797ordA"
    
    #url = "https://api.spotify.com/v1/recommendations?seed_genres=alt-rock,alternative,folk,rock"

    url = f"https://api.spotify.com/v1/recommendations?seed_tracks={track_id}"

    access_token = get_token().get('access_token')

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {access_token}"
    }

    response = requests.get(url, headers = headers)

    return response.json()

def search(search_term = "clay%20pigeons", music_type = "track,album", limit = 5):
    #sleep to not go over api request limit
    time.sleep(1.5)
    #turn spaces into %20
    if search_term.find(" ") != -1:
        search_term = search_term.replace(' ', '%20')
    if search_term.find('&') != -1:
        search_term = search_term.replace('&', '%26')
    print(search_term)
        
    url = f"https://api.spotify.com/v1/search?q={music_type}:{search_term}&type={music_type}&limit={limit}"

    access_token = get_token().get('access_token')
    
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)

    return response.json()

def get_recs(**kwargs):
    if kwargs.get('mode') == "search":
        search_response = search(search_term = kwargs.get('name'), music_type = 'track')
        rec_id = search_response.get('tracks').get('items')[0].get('id')

        recs = recommendations(track_id=rec_id)
        return recs




def get_new_releases(country = "US", limit = 20, offset = 0):
    url = f"https://api.spotify.com/v1/browse/new-releases?country={country}&limit={limit}&offset={offset}"

    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    return response.json().get('albums').get('items')

#
def get_album(id = '2T1qRB6zSSGdNgcTD3Dg8H', market = 'US'):
    time.sleep(3)
    url = f"https://api.spotify.com/v1/albums/{id}"

    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    return response.json().get('tracks').get('items')



#program get audio features function

def audio_features(track_id = "4nFAL2TKUOoAPQJ5DGGoTd"):
    time.sleep(3)
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    
    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)

    return response.json()

def get_several_albums(ids, market = "US"):
    url = f"https://api.spotify.com/v1/albums?ids={ids}"

    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    return response.json().get('albums')

def get_several_tracks(ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ"):
    url = f"https://api.spotify.com/v1/tracks?ids={ids}"

    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    return response.json()

    




def new_release_features(limit = 20, offset = 0, country = "US"):

    new_release_albums = get_new_releases(country = "US",
                                          limit = limit,
                                          offset = offset)
    #get album ids out of the new release response to pass to get album
    album_ids = [alb.get('id') for alb in new_release_albums]
    #create request string for get several albums
    album_request_string = ""
    for index, id in enumerate(album_ids):
        if index != (len(album_ids) - 1):
          album_request_string += (id + ',')
        else:
            album_request_string += id
    #call several albums
    albums = get_several_albums(ids = album_request_string)

    data  =[]
    #get track data for each track
    for alb in albums:
        alb_tracks = alb.get('tracks').get('items')
        for track in alb_tracks:
            track_ids = [track.get('id') for track in alb_tracks]
            for id in track_ids:
                features = audio_features(track_id=id)
                data.append(features)
    return data
        
def get_playlist_tracks(playlist_id,offset):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?offset={offset}"
    access_token = get_token().get('access_token')

    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)

    return response.json()

def find_average_song(
    seed_tracks="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ", 
    limit = 1,
    market="US",
    acousticness=.5,
    danceability=.5,
    energy=.5,
    instrumentalness=.5,
    liveness = .5,
    speechiness = .5,
    valence=.4,
):

    url = f"""
    https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks}&limit={limit}&market={market}&target_acousticness={acousticness}
    """
    access_token = get_token().get('access_token')
    
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    
    return response.json()













        
