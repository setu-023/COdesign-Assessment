
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/setu-023/COdesign-Assessment
```

Create a virtual environment to install dependencies and activate it(OS:mac/linux):

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment is set up.

Once `pip` has finished downloading the dependencies run these commands to update database:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

For creating a superuser run this command:
```sh
(env)$ python manage.py createsuperuser
```

And finaly, Its ready to run:
```sh
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

APIs:

*  **Login:**  POST http://127.0.0.1:8000/log-in/

**Required Fields: username, password**
```sh
body sample: 

{
    "username": "akkan",
    "password": "aa"
}

```

From login request, a token will be returned. Add this token in the request header for making POST request:
```sh
Authorization: Token 610924f6d133e412a8227cb558e39dab51d61a08
```


*  **Get All Public Paletee:**  GET http://127.0.0.1:8000/palettes
```sh
body sample: 
```

*  **Create A Palette:**  POST http://127.0.0.1:8000/palettes/

**Required Fields: name(must be unique), dominant_color, accent_color**

```sh

body sample: 

{
    "name": "test3",
    "dominant_color": [
        1,
        2
    ],
    "accent_color": [
        3,
        4,
        5
    ]
}

```

*  **Publish/Private A Palette:**  POST http://127.0.0.1:8000/palettes/publish/

**Required Fields: palette_id, is_public**
```sh
body sample: 
{
    "palette_id": 27,
    "is_public": false
}

```


*  **Create Favorite Palette:**  POST http://127.0.0.1:8000/palettes/favorite/

**Required Fields: palette**

```sh
body sample: 
{
    "palette": 27
}
```

*  **GET Favorite Palette:**  GET http://127.0.0.1:8000/palettes/favorite/
```sh
body sample: 
```

*  **Search Palette:**  GET http://127.0.0.1:8000/palettes/search/?q=Y
```sh
body sample: 
```