from flask import request
import tkinter as tk

def getNews():
    api_key = "7a3c09fb3244468b98c77049569f22ff"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api_key
    news = requests.get(url).json()
    articles = news["articles"]
    # fetch the title of the articles
    my_articles_titles = []
    my_news = ""
    for article in articles:
        my_articles_titles.append(article["title"])
    
    for i in range(10):
        my_news = my_news + my_articles_titles[i] + "\n"

    print(my_news)


canvas = tk.TK()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 25, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

canvas.mainloop()
