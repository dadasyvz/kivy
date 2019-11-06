from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
import sqlite3 as sql
import random

tvt = sql.connect("C:\\Users\\Gebruiker\\Desktop\\proje.db")
tim = tvt.cursor()

class MainScreen(ScreenManager):
    pass

class Db(Screen):
    def Goster(self, metin):
        liste = []
        a = list(tim.execute("SELECT * FROM ----- where tip=?", (-----,)))
        for i in a:
            liste.append(i[0])
        self.display.text = random.choice(liste)


class User(Screen):
    pass

class Log(Screen):
    pass

class Login(App):
    def build(self):
        self.title="Main Screen"
        return MainScreen()

if __name__ == '__main__':
    Login().run()
