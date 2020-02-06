import requests
import pprint

class news():
    def __init__(self, search):
        url = '8ee604fc64ab4e11a2dcf416dad64ac4'
        self.conn = requests.get(f"https://newsapi.org/v2/everything?q={search}&apiKey={url}")
        self.news_json = self.conn.json()
        print(self.news_json['articles'])
    def news1(self):
        news_json = self.news_json
        title = news_json['articles'][0]['title']
        newsUrl = news_json['articles'][0]['url']
        author = news_json['articles'][0]['author']
        final_str = '%s \nurl: %s \nauthor: %s' % (title, newsUrl, author)
        return final_str
    def news2(self):
        news_json = self.news_json
        title = news_json['articles'][1]['title']
        newsUrl = news_json['articles'][1]['url']
        author = news_json['articles'][1]['author']
        final_str = '%s \nurl: %s \nauthor: %s' % (title, newsUrl, author)
        return final_str
    def news3(self):
        news_json = self.news_json
        title = news_json['articles'][2]['title']
        newsUrl = news_json['articles'][2]['url']
        author = news_json['articles'][2]['author']
        final_str = '%s \nurl: %s \nauthor: %s' % (title, newsUrl, author)
        return final_str
    def news4(self):
        news_json = self.news_json
        title = news_json['articles'][3]['title']
        newsUrl = news_json['articles'][3]['url']
        author = news_json['articles'][3]['author']
        final_str = '%s \nurl: %s \nauthor: %s' % (title, newsUrl, author)
        return final_str
    def news5(self):
        news_json = self.news_json
        title = news_json['articles'][4]['title']
        newsUrl = news_json['articles'][4]['url']
        author = news_json['articles'][4]['author']
        final_str = '%s \nurl: %s \nauthor: %s' % (title, newsUrl, author)
        return final_str


# test scroll
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# container = ttk.Frame(root)
# canvas = tk.Canvas(container)
# scrollbar = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
# scrollable_frame = ttk.Frame(canvas)
#
# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )
#
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#
# canvas.configure(xscrollcommand=scrollbar.set)
#
# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
#
# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="bottom", fill="x")
#
# root.mainloop()