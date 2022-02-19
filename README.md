# Руководство Django Girls

Пройдено [Руководство Django Girls](https://tutorial.djangogirls.org/ru/).

Также пройдено продолжение по [Django Girls Tutorial: Extensions](https://tutorial-extensions.djangogirls.org/).

Сайт развёрнут на сервере [Pythonanywhere](https://www.pythonanywhere.com) и доступен по адресу <https://zelo78.pythonanywhere.com/>

Дополнительно:

- Использование `.env` файла для хранения настроек и секретной информации
- Использование [Flatpages](https://docs.djangoproject.com/en/4.0/ref/contrib/flatpages/ "Простые страницы") для статичных страниц
- Добавлен WYSIWYG-редактор [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor) для редактирования Flatpages в интерфейсе администрирования (с переопределением класса `FlatPageAdmin`)

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.2
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.19.2 - Считывает пары ключ-значение из файла .env и может устанавливать их в качестве переменных среды
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) v. 6.2.0

## Использованные технологии и программы

- Git, [GitHub](https://github.com/zelo78/), [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)

### TODO

- Полный переход на Class-Based Views
- Генерация случайного наполнения демонстрационной базы
- Использование permissions
- Использование bootstrap 5
- Изменение дизайна страницы
- header и footer в шаблонах
- Кеширование
- Переход на Postgresql 
- Авторизация через социальные сети
- Наследование моделей
- Фильтрация и пагинация в списке постов
- Текстовый поиск в постах
- robots.txt, sitemap.xml
- django-constance
