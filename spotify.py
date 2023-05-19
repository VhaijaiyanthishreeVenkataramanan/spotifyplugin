import spotipy
import json
import webbrowser

username = 'up392ljvem07p9z4q4mqmieiw'
clientID = '7e18d126251545e39c672edc01cd6784'
clientSecret = '3fb9525259a9465385f360528f04e7a2'
redirectURI ='http://google.com/'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

print(json.dumps(user,sort_keys=True, indent=4))

while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        # Get the Song Name.
        searchQuery = input("Enter Song Name: ")
        # Search for the Song.
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif choice == 0:
        break
    else:
        print("Enter valid choice.")