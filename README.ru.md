# spotify-to-csv-export-script
Скрипт для экспорта информации (uri, название, исполнители, альбом, продолжительность) сохраненных треков и плейлистов пользователя Spotify.

На основе библиотеки [Tekore](https://github.com/felix-hilden/tekore) (клиент Spotify Web API).

*Читать на других языках: [English](README.md), [Русский](README.ru.md).*

[Scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/) (области, к которым скрипт получает доступ):
- user-read-email, для ```spotify.current_user().id```
- user-library-read 
- playlist-read-collaborative 
- playlist-read-private

## Как использовать:
1. Клонируйте репозиторий:
~~~bash
$ git clone https://github.com/egliorn/spotify-to-csv-export-script
~~~
2. Смените директорию:
~~~bash
$ cd spotify-to-csv-export-script
~~~
3. Установите зависимости:
~~~bash
$ pip install -r requirements.txt
~~~
5. Войдите в https://developer.spotify.com/dashboard/ (нужен аккаунт Spotify).


6. `CREATE AN APP` -> укажите имя приложения и описание -> `CREATE`.


7. Появится обзор приложения, которое вы создали.


8. Скопируйте `Client ID`, `Client Secret`(SHOW CLIENT SECRET).


9. Вставьте значения в соответствующие переменные в начале `script.py` `CLIENT_ID`, `CLIENT_SECRET`


10. Запустите приложение:
~~~bash
$ python script.py
~~~

### Импорт экспортированных треков/плейлистов
:exclamation: Работает только в приложении Spotify.

После сохранения плейлистов:
1. Создайте плейлист в Spotify.
2. Скопируйте из `название_плейлиста.csv` значения колонны `track_uri` 
(пример значения: `spotify:track:2FJyRsWesaxh5nOTDQWBMw`).
3. Вставьте в страничку плейлиста.

## Как это работает:
1. Приложение открывает веб-браузер для входа в Spotify.
2. После того как пользователь войдет в систему и предоставит доступ -> пользователь копирует полученный URL-адрес и вставит его в командную строку.
3. Приложение получает токен пользователя Spotify из вставленного URL-адреса *code и *state args. Затем сохраняет его в tekore.cfg
4. Проверяет, существует ли ./export. Если нет -> создает ./export
5. Получает сохраненные треки и плейлисты текущего пользователя Spotify.
6. Сохраняет сохраненные треки и плейлисты в ./export в формате .csv
