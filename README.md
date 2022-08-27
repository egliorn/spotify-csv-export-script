# spotify-to-csv-export-script
A script, for exporting saved tracks and playlists of a Spotify user.
Based on [Tekore](https://github.com/felix-hilden/tekore) library (Spotify Web API client).

Used [scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/):
- user-read-email, for ```spotify.current_user().id```
- user-library-read 
- playlist-read-collaborative 
- playlist-read-private

---
### How it works:
1. App opens web browser to log in Spotify
2. After the user logs in and grants access -> user copies the redirect url and pastes it into the command prompt
3. App gets Spotify user token, from pasted url *code and *state args. Then saves it into tekore.cfg
4. Checks, if ./export exists. If not -> creates ./export
5. Gets current users Spotify saved tracks and playlists
6. Saves saved tracks and playlists into ./export in .csv format
