[app]

# Название приложения
title = KoreaVibe

# Имя пакета Android: только латинские буквы и цифры
package.name = koreavibe

# Уникальный домен проекта
package.domain = org.koreavibe

# Версия приложения
version = 0.1.0

# Папка проекта
source.dir = .

# Файлы, которые должны попасть в приложение
source.include_exts = py,kv,png,jpg,jpeg,atlas,txt,json

# Папки, которые не нужно включать
source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__

# Зависимости Python/Kivy
requirements = python3,kivy

# Ориентация экрана
orientation = portrait

# Не создаём полноэкранный режим принудительно
fullscreen = 0

# Автоматически принять лицензию Android SDK
android.accept_sdk_license = True

# Для первой учебной сборки достаточно современных 64-битных устройств
android.archs = arm64-v8a

# Имя APK можно определить через version и package.name
# Сборка: buildozer -v android debug

[buildozer]

# Логи сборки
log_level = 2

# Предварительно заданная команда
# buildozer android debug
