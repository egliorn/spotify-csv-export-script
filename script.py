import tekore as tk
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
    playlists_ids = [playlist.id for playlist in user_playlists.items]

    return [spotify.playlist(playlist_id).tracks for playlist_id in playlists_ids]


def playlist_unpack(track_paging):
    """unpacks the contents of given 'SavedTrackPaging' or 'PlaylistTrackPaging'"""
    contents = []
    for item in spotify.all_items(track_paging):
        contents.append(
            {
                'track_name': item.track.name,
                'artists': ",".join([artist.name for artist in item.track.artists]),
                'album': item.track.album.name,
                'duration': f"{round(item.track.duration_ms / 1000)}sec"
            }
        )

    return contents


token = get_user_token()
spotify = tk.Spotify(token)
