Final projcet to implement a server with end points that allow to translate from English to French and from French to English.


# Setup

Python packages using in this project:
```console
$ python3 -m pip install python-dotenv
$ python3 -m pip install ibm_watson
$ python3 -m pip install Flask
```

Set the `apikey` and the `url` of your IBM Language Translator instance using the file `final_project/machinetranslation/.env`.

# Server

A web based language translator service using IBM Watson API.

```console
$ cd final_project/
$ python server.py
```
Check the URL [http://127.0.0.1:8080](http://127.0.0.1:8080).

# Test Unit

```console
$ cd final_project/machinetranslation
$ python -m unittest tests/test_translator.py
```
