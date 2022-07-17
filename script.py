import tekore as tk
from pandas import DataFrame
import os


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


def get_user_token():
    """:returns user token and saves to ./tekore.cfg"""
    if not os.path.exists('tekore.cfg'):
        user_token = tk.prompt_for_user_token(
            CLIENT_ID,
            CLIENT_SECRET,
            REDIRECT_URI,
            scope=tk.scope.every
        )

        conf = (CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, user_token.refresh_token)
        tk.config_to_file('tekore.cfg', conf)

    conf = tk.config_from_file('tekore.cfg', return_refresh=True)
    return tk.refresh_user_token(*conf[:2], conf[3])


def get_saved_tracks():
    """:returns user's saved tracks, 'SavedTrackPaging'"""
    return spotify.saved_tracks()


def get_saved_playlists():
    """:returns a list of all user's playlists, 'PlaylistTrackPaging'"""
    user_id = spotify.current_user().id
    user_playlists = spotify.playlists(user_id=user_id)
    playlists_ids = [pl.id for pl in user_playlists.items]

    return [spotify.playlist(playlist_id) for playlist_id in playlists_ids]


def playlist_unpack(track_paging):
    """unpacks the contents of given 'SavedTrackPaging' or 'PlaylistTrackPaging'"""
    contents = []
    for item in spotify.all_items(track_paging):
        contents.append(
            {
                "track_name": item.track.name,
                "artists": ",".join([artist.name for artist in item.track.artists]),
                "album": item.track.album.name,
                "duration": f"{round(item.track.duration_ms / 1000)}sec"
            }
        )

    return contents


def save_to_csv(playlist_contents_to_save, playlist_name):
    """saves the contents of the playlist to a /export/*name*.csv file with the given playlist name"""
    dataframe = DataFrame(playlist_contents_to_save)
    dataframe.to_csv(f'./export/{playlist_name}.csv', encoding='utf-8', index=False)


token = get_user_token()
spotify = tk.Spotify(token)

# creating path /export if not already exists
if not os.path.exists('./export'):
    os.makedirs('./export')

# exporting saved tracks
saved_tracks_contents = playlist_unpack(get_saved_tracks())
save_to_csv(saved_tracks_contents, "saved tracks")

# exporting saved playlists
for playlist in get_saved_playlists():
    playlist_contents = playlist_unpack(playlist.tracks)
    save_to_csv(playlist_contents, playlist.name)
