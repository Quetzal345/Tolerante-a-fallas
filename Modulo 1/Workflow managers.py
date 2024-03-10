import requests
from threading import Thread
import time

token = 'BQD5v6_C6g9eMfQJ2SBAHpLMq7iOzWdAKV86DMeY3nge78O3hUiq7X_n1ra6fABJZDkYYwS_b8v0vVbqVR8w5TyQMgCWZf6NTPUiih21tLJr_UoigwJfZvaOAHW_wmnTR2aFxbehkB2265PnYz7DnECMJRdAAPMFdRYr-J8H3uQj_lVkQWR7Ji9IXLBJDyFS7I-cE59H8Ni1NepMQobxFXWiPLV30SNQpf0-5ep5G83ftLNaMQtUVYJmzeLcvA-XJPCd89K-9zA7O1PHdyE2pE5q';

def fetch_web_api(endpoint, method='GET', body=None, retries=3, delay=5):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    if body:
        headers['Content-Type'] = 'application/json'
    url = f'https://api.spotify.com/{endpoint}'
    while retries > 0:
        response = requests.request(method, url, headers=headers, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            
            print(f"Error: {response.status_code}, {response.text}")
            time.sleep(delay)
            retries -= 1
    return None

def get_top_tracks():
    # Limite de 50
    return fetch_web_api('v1/me/top/tracks?time_range=long_term&limit=50')

def print_top_tracks():
    top_tracks = get_top_tracks()
    if top_tracks and 'items' in top_tracks:
        print('\n'.join([f"{track['name']} por {', '.join([artist['name'] for artist in track['artists']])}" for track in top_tracks['items']]))
    else:
        print("Error obteniendo las canciones principales.")

# Crear y comenzar un hilo para obtener las canciones principales
thread = Thread(target=print_top_tracks)
thread.start()
thread.join()
