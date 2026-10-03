from kivy.uix.screenmanager import Screen
from database import check_user

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text

        if not username or not password:
            self.ids.message.text = "Заполните все поля"
            return # позволяет закончить выполнение текущего метода

        # Проверяем пользователя
        if check_user(username, password):
            # Переходим в приложение
            self.manager.current = "main"
        else:
            self.ids.message.text = (
                "Неверное имя пользователя или пароль"
                )
