Spotify Playlist

##### This repo contains all the `project files`.

Installation

1 - clone repo https://github.com/DavidDanso/Spotify_Playlist
2 - create a virtual environment and activate
pip install virtualenv
virtualenv envname
source envname\scripts\activate`[for Mac users]`

`Imports`
##### - requests, BeautifulSoup, spotipy, SpotifyOAuth

## Project Description

#### A GUI Application that creates a Spotify Playlist from any year in the past, by just entering your preferred date 

## Authentication with Spotify
1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, 
you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/create_app_img.png" width=600 />

3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/secret_key_img.png" width=600 />

`Authenticating with Spotify is quite complicated, especially when you want to access a user's account. So use, 
one of the most popular Python Spotify modules - SPOTIPY to make things easier.`

3.1. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). 
As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/edit_img.png" width=600 />
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/redirect_url_img.png" width=600 />

4. Run the program and wait for a while, but first make sure your have your `Client ID and Client Secret` stored into a variable provided in the program
HINT 4:  If successful, you should see the page below show up automatically (be sure to click Agree):
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/agree_img.png" width=600 />

5. You'll get a new URL copy the entire URL from the address bar, finally you need to paste the URL into the prompt in PyCharm:
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/URL.png" width=600 />
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/agree_img.png" width=600 />

6. Now if you close PyCharm and restart, you should see a new file in this project called token.txt
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/images/token_img.png" width=600 />


## Project UI
<img src="https://github.com/DavidDanso/Spotify_Playlist/blob/master/UI.png" width=600 />

### Happy Scraping!
