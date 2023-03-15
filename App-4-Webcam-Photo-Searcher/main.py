import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from bs4 import BeautifulSoup
import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # get text input
        query = self.manager.current_screen.ids.user_query.text
        # get wiki page and the list of image urls
        search = wikipedia.search(query)
        try:
            page = wikipedia.page(search[0], auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as e:
            for link in e.options:
                try:
                    page = wikipedia.page(link, auto_suggest=False)
                except wikipedia.exceptions.PageError:
                    # if a "PageError" was raised, ignore it and continue to next link
                    continue
        image_link = page.images[0]
        print(image_link)
        return image_link

    def download_image(self):
        # download the image
        req = requests.get(self.get_image_link(), "lxml")
        imagepath = 'F:\Python\OOP\App-4-Webcam-Photo-Sharer\image.jpg'
        with open('image.jpg', 'wb') as file:
            file.write(req.content)
        # set the image in the Image Widget
        return imagepath

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()