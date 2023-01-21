# spotify-to-csv-export-script
A script, for exporting saved tracks and playlists of a Spotify user (uri, name, artists, album, duration).
Based on [Tekore](https://github.com/felix-hilden/tekore) library (Spotify Web API client).

*Read this in other languages: [English](README.md), [Русский](README.ru.md).*

## Used [scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/):
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
4. Sign in to https://developer.spotify.com/dashboard/ (Spotify account required).
5. `CREATE AN APP` -> provide an application name and description -> `CREATE`.
6. An overview of the app you created will appear.
7. Copy `Client ID`, `Client Secret`(SHOW CLIENT SECRET).
8. Insert values into appropriate variables at the beginning of `script.py`: `CLIENT_ID`, `CLIENT_SECRET`.
9. Run the application:
~~~bash
$ python script.py
~~~
10. A new browser tab will appear. With authorization, and an agreement to view the account data that the script has access to (read [used scopes](#spotify-to-csv-export-script)).
11. After authorization and agreement (ACCEPT) -> you will be redirected to a URL like `http://localhost:5000/callback?code=***`.
12. Copy the URL and paste in `Please paste redirect URL:` in the script execution window.
13. A `tekore.cfg` file and a `/export` folder will appear with your playlists in .csv.

Items 10, 11, 12 are not needed at the next script launches. Spotify token will be updated automatically.

#### :grey_exclamation: Note if you are using MS Excel:
If you use Excel to open `playlist_name.csv` - non-english characters may be displayed in incorrect encoding.
To fix this – use different app or check this solutions:
- https://stackoverflow.com/a/6488070
- [https://answers.microsoft.com/](https://answers.microsoft.com/en-us/msoffice/forum/all/how-to-open-utf-8-csv-file-in-excel-without-mis/1eb15700-d235-441e-8b99-db10fafff3c2)

### Import exported playlists to Spotify
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
