from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from database import create_database
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.main_screen import MainScreen

class KoreaVibeApp(App):
    def build(self):
        create_database()
      
        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/main_screen.kv")
        Builder.load_file("kv/register.kv")

        screen_manager = ScreenManager()
        screen_manager.add_widget(
          LoginScreen(name = "login")
        )
        screen_manager.add_widget(
          RegisterScreen(name = "register")
        )
        screen_manager.add_widget(
          MainScreen(name = "main")
        )
        return screen_manager

if __name__ == "__main__":
    KoreaVibeApp().run()
