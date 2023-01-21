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
4. Войдите в https://developer.spotify.com/dashboard/ (нужен аккаунт Spotify).
5. `CREATE AN APP` -> укажите имя приложения и описание -> `CREATE`.
6. Появится обзор приложения, которое вы создали.
7. Скопируйте `Client ID`, `Client Secret`(SHOW CLIENT SECRET).
8. Вставьте значения в соответствующие переменные в начале `script.py` `CLIENT_ID`, `CLIENT_SECRET`.
9. Запустите приложение:
~~~bash
$ python script.py
~~~
10. Появится новая вкладка в браузере с авторизацией и соглашением на просмотр данных аккаунта, к которым скрипт получает доступ (см. Scopes).
11. После авторизации и соглашения (ПРИНИМАЮ) -> вы будете перенаправлены на URL с видом `http://localhost:5000/callback?code=***`.
12. Скопируйте URL и вставьте в `Please paste redirect URL: ` в окне выполнения скрипта.
13. Появятся файл `tekore.cfg` и папка `/export` с вашими плейлистами в .csv.

При следующих запусках скрипта пункты 10, 11, 12 не нужны. Tокен Spotify будет обновляться автоматически.

#### :grey_exclamation: Если вы используете MS Excel:

Если вы используете Excel для открытия `playlist_name.csv`, "неанглийские" символы могут отображаться в неправильной кодировке.

Чтобы это исправить — используйте другое приложение или попробуйте эти решения:
- https://stackoverflow.com/a/6488070
- [https://answers.microsoft.com/](https://answers.microsoft.com/en-us/msoffice/forum/all/how-to-open-utf-8-csv-file-in-excel-without-mis/1eb15700-d235-441e-8b99-db10fafff3c2)

### Импорт экспортированных плейлистов в Spotify
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
6. Сохраняет сохраненные треки и плейлисты в ./export в формате .csv.
