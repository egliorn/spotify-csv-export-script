# spotify-to-csv-export-script
A script, for exporting saved tracks and playlists of a Spotify user (name, artists, album, duration).
Based on [Tekore](https://github.com/felix-hilden/tekore) library (Spotify Web API client).

*Read this in other languages: [English](README.md), [Русский](README.ru.md).*

Used [scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/):
- user-read-email, for ```spotify.current_user().id```
- user-library-read 
- playlist-read-collaborative 
- playlist-read-private

## How to use:
1. Clone the repository:
~~~bash
$ git clone https://github.com/egliorn/spotify-to-csv-export-script
~~~
2. Change directory:
~~~bash
$ cd spotify-to-csv-export-script
~~~
3. Install dependencies:
~~~bash
$ pip install -r requirements.txt
~~~
5. Sign in to https://developer.spotify.com/dashboard/ (Spotify account required).


6. `CREATE AN APP` -> provide an application name and description -> `CREATE`.


7. An overview of the app you created will appear.


8. Copy `Client ID`, `Client Secret`(SHOW CLIENT SECRET).


9. Insert values into appropriate variables at the beginning of `script.py` `CLIENT_ID`, `CLIENT_SECRET`


10. Run the application:
~~~bash
$ python script.py
~~~

### Import exported tracks/playlists
:exclamation: **Only works in the Spotify desktop app**.

After saving playlists:
1. Create a playlist in Spotify.
2. Copy from `playlist_name.csv` the values of the `track_uri` column
(example value: `spotify:track:2FJyRsWesaxh5nOTDQWBMw`).
3. Paste into the playlist page.



### How it works:
1. App opens web browser to log in Spotify
2. After the user logs in and grants access -> user copies the redirect url and pastes it into the command prompt
3. App gets Spotify user token, from pasted url *code and *state args. Then saves it into tekore.cfg
4. Checks, if ./export exists. If not -> creates ./export
5. Gets current users Spotify saved tracks and playlists
6. Saves saved tracks and playlists into ./export in .csv format
