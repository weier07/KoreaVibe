from kivy.uix.screenmanager import Screen
from database import register_user

class RegisterScreen(Screen):
    def register(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text
        password2 = self.ids.password2.text

        if not username or not password or not password2:
            self.ids.message.text = "Заполните все поля"
            return  # позволяет закончить выполнение текущего метода

        # Проверяем пароли
        if password != password2:
            self.ids.message.text = "Пароли не совпадают"
            return
        if len(password) < 4:
            self.ids.message.text = (
                "Пароль должен содержать минимум 4 символа"
            )
            return

        # Создаём пользователя
        if register_user(username, password):
            # Переходим в приложение
            self.manager.current = "main"

        else:
            self.ids.message.text = (
                "Такое имя пользователя уже существует"
                )
