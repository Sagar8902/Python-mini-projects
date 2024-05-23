import requests

class NewsApp:

    def __init__(self):

        #fetch data
        data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=c17af33e0188485bac7cc6f6de54ddee").json()
        print(data)
        #initial GUI load
        #load the 1st news

obj = NewsApp()
