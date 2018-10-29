import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "9d701922a7fd4955b3e8c82046fc82d4"
cs = "70a8506178a34ef093788e25e196ab50"

client_credentials = SpotifyClientCredentials(client_id=cid, client_secret=cs, proxies=None)

token = client_credentials.get_access_token()
print(token)

sp = spotipy.Spotify(auth=token, client_credentials_manager=client_credentials)

track_id = "spotify:track:0cjvRZVV217eDcZXXTHxBl"
print(sp.track(track_id))
