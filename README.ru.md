# spotify-to-csv-export-script
Скрипт для экспорта сохраненных треков и плейлистов пользователя Spotify.
На основе библиотеки [Tekore](https://github.com/felix-hilden/tekore) (клиент Spotify Web API).

*Читать на других языках: [English](README.md), [Русский](README.ru.md).*

[Scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/) (области, к которым скрипт получает доступ):
- user-read-email, для ```spotify.current_user().id```
- user-library-read 
- playlist-read-collaborative 
- playlist-read-private

---
### Как это работает:
1. Приложение открывает веб-браузер для входа в Spotify.
2. После того как пользователь войдет в систему и предоставит доступ -> пользователь копирует полученный URL-адрес и вставит его в командную строку.
3. Приложение получает токен пользователя Spotify из вставленного URL-адреса *code и *state args. Затем сохраняет его в tekore.cfg
4. Проверяет, существует ли ./export. Если нет -> создает ./export
5. Получает сохраненные треки и плейлисты текущего пользователя Spotify.
6. Сохраняет сохраненные треки и плейлисты в ./export в формате .csv
