import tekore as tk
import csv
import os

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPES = [
    'user-read-email',  # for spotify.current_user().id
    'user-library-read',
    'playlist-read-collaborative',
    'playlist-read-private',
]


def get_user_token():
    """:returns user token and saves to ./tekore.cfg"""
    if not os.path.exists('tekore.cfg'):
        user_token = tk.prompt_for_user_token(
            CLIENT_ID,
            CLIENT_SECRET,
            REDIRECT_URI,
            scope=SCOPES
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
    """:returns the contents of given 'SavedTrackPaging' or 'PlaylistTrackPaging'"""
    playlist_contents = [["track_uri", "track_name", "artists", "album", "duration"]]
    for item in spotify.all_items(track_paging):
        playlist_contents.append(
            [
                item.track.uri,
                item.track.name,
                ", ".join([artist.name for artist in item.track.artists]),
                item.track.album.name,
                f"{round(item.track.duration_ms / 1000)}sec"
            ]
        )

    return playlist_contents


def save_to_csv(playlist_contents, playlist_name):
    """saves the contents of the playlist to a /export/playlist_name.csv"""
    with open(f"./export/{playlist_name}.csv", 'w', encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in playlist_contents:
            writer.writerow(row)


token = get_user_token()
spotify = tk.Spotify(token)

# creating path /export if not already exists
if not os.path.exists("./export"):
    os.makedirs("./export")

# exporting saved tracks
saved_tracks_contents = playlist_unpack(get_saved_tracks())
save_to_csv(saved_tracks_contents, "Liked Songs")

# exporting saved playlists
for playlist in get_saved_playlists():
    contents = playlist_unpack(playlist.tracks)
    save_to_csv(contents, playlist.name)
