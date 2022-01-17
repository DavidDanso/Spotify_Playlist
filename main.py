import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from message import MESSAGE

message = MESSAGE
# ---------------------------- CODES ------------------------------- #
SPOTIFY_CLIENT_ID = "PASTE_YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "PASTE_YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://example.com"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

# ---------------------------- UI SETUP ------------------------------- #
MAIN_COLOR = "#1db954"
SECONDARY_COLOR = "#282828"
FONT_NAME = "Ariel"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Scraping Billboard")
window.config(padx=30, pady=20)

# Billboard Canvas
billboard_canvas = Canvas(width=200, height=90)
billboard_png = PhotoImage(file="./images/billboard.png").subsample(11, 11)
billboard_canvas.create_image(100, 15, image=billboard_png)
billboard_canvas.grid(row=0, column=1)

# Arrow Canvas
arrow_canvas = Canvas(width=200, height=90)
arrow_png = PhotoImage(file="./images/arrow.png").subsample(22, 22)
arrow_canvas.create_image(80, 20, image=arrow_png)
arrow_canvas.grid(row=0, column=2)

# Spotify Canvas
spotify_canvas = Canvas(width=200, height=90)
spotify_png = PhotoImage(file="./images/spotify_logo.png").subsample(17, 17)
spotify_canvas.create_image(70, 20, image=spotify_png)
spotify_canvas.grid(row=0, column=3)

def info():
    messagebox.showinfo(message=f"{message}")

info_button = Button(window, text="Read Program Info", command=info, fg=SECONDARY_COLOR,
                     highlightbackground="#e82c2a", highlightthickness=0, font=(FONT_NAME, 13))
info_button.config(padx=5, pady=5)
info_button.grid(row=1, column=1, columnspan=3)


# Date Widgets
date_label = Label(text="Date[ YYYY-MM-DD ]:", font=(FONT_NAME, 15), fg=MAIN_COLOR)
date_label.config(padx=0, pady=7)
date_label.grid(row=2, column=1)

date_field = Entry(width=30, highlightthickness=0, font=(FONT_NAME, 15), fg=MAIN_COLOR)
date_field.grid(row=2, column=2)
date_field.focus()

date_canvas = Canvas(width=200, height=50)
date_image = PhotoImage(file="./images/date.png").subsample(12, 12)
date_canvas.create_image(40, 20, image=date_image)
date_canvas.grid(row=2, column=3)

# URL Widgets
url_label = Label(text="Billboard URL:", font=(FONT_NAME, 15), fg=MAIN_COLOR)
url_label.config(padx=0, pady=7)
url_label.grid(row=3, column=1)

url_field = Entry(width=30, highlightthickness=0, font=(FONT_NAME, 15), fg=MAIN_COLOR)
url_field.grid(row=3, column=2)
url_field.insert(0, BILLBOARD_URL)


url_canvas = Canvas(width=200, height=50)
billboard_image = PhotoImage(file="./images/b_logo.png").subsample(17, 17)
url_canvas.create_image(40, 20, image=billboard_image)
url_canvas.grid(row=3, column=3)

# Client Id Widgets
id_label = Label(text="Spotify Client ID:", font=(FONT_NAME, 15), fg=MAIN_COLOR)
id_label.config(padx=0, pady=7)
id_label.grid(row=4, column=1)

id_field = Entry(width=30, highlightthickness=0, font=(FONT_NAME, 15), fg=MAIN_COLOR)
id_field.grid(row=4, column=2)
id_field.insert(0, SPOTIFY_CLIENT_ID)

id_canvas = Canvas(width=200, height=50)
client_id_image = PhotoImage(file="./images/ID.png").subsample(15, 15)
id_canvas.create_image(40, 25, image=client_id_image)
id_canvas.grid(row=4, column=3)

# Client Secret Widgets
client_secret_label = Label(text="Spotify Secret Code:", font=(FONT_NAME, 15), fg=MAIN_COLOR)
client_secret_label.config(padx=0, pady=7)
client_secret_label.grid(row=5, column=1)

client_secret_field = Entry(width=30, highlightthickness=0, font=(FONT_NAME, 15), fg=MAIN_COLOR)
client_secret_field.grid(row=5, column=2)
client_secret_field.insert(0, SPOTIFY_CLIENT_SECRET)

client_secret_canvas = Canvas(width=200, height=50)
client_secret_image = PhotoImage(file="./images/secret.png").subsample(15, 15)
client_secret_canvas.create_image(40, 25, image=client_secret_image)
client_secret_canvas.grid(row=5, column=3)

# Redirect URL Widgets
redirect_url_label = Label(text="Redirect URL Link:", font=(FONT_NAME, 15), fg=MAIN_COLOR)
redirect_url_label.config(padx=0, pady=7)
redirect_url_label.grid(row=6, column=1)

redirect_url_field = Entry(width=30, highlightthickness=0, font=(FONT_NAME, 15), fg=MAIN_COLOR)
redirect_url_field.grid(row=6, column=2)
redirect_url_field.insert(0, SPOTIFY_REDIRECT_URI)

url_canvas = Canvas(width=200, height=50)
url_image = PhotoImage(file="./images/URL.png").subsample(17, 17)
url_canvas.create_image(40, 25, image=url_image)
url_canvas.grid(row=6, column=3)

# Scrap Button
def scrap_btn():
    date = date_field.get()
    url = url_field.get() + date
    spotify_redirect_url = redirect_url_field.get()
    spotify_client_id = id_field.get()
    spotify_client_secret = client_secret_field.get()

    response = requests.get(url)
    html_file = response.text
    soup = BeautifulSoup(html_file, "html.parser")
    song_title = [title.getText().replace("\n", "") for title in soup.find_all(name="h3", class_="a-no-trucate")]
    print("SCRAPING HAS STARTED...\nWAIT FOR A MINUTE!")

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=spotify_redirect_url,
            client_id=spotify_client_id,
            client_secret=spotify_client_secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    song_uris = []
    year = date.split("-")[0]
    for song in song_title:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            with open('not_found.txt', mode="a") as file:
                file.write(f"{song} doesn't exist in Spotify. Skipped.\n")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    print(f"Check your spotify app for your {date} playlist")

info_button = Button(window, text="Create Playlist", command=scrap_btn, fg=SECONDARY_COLOR,
                     highlightbackground=MAIN_COLOR, highlightthickness=0, font=(FONT_NAME, 13))
info_button.config(padx=5, pady=5)
info_button.grid(row=7, column=1, columnspan=3)

window.mainloop()

