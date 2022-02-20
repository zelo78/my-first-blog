# Руководство Django Girls

Пройдено [Руководство Django Girls](https://tutorial.djangogirls.org/ru/).

Также пройдено продолжение по [Django Girls Tutorial: Extensions](https://tutorial-extensions.djangogirls.org/).

После прохождения обучения в [Лаборатории Django-разработки](https://thinknetica.com/django_lab), в проект были включены основные моменты, освоенные в ходе обучения. 

Сайт развёрнут на сервере [Pythonanywhere](https://www.pythonanywhere.com) и доступен по адресу <https://zelo78.pythonanywhere.com/>

Исходный код доступен на [GitHub](https://github.com/zelo78/my-first-blog)

## Дополнительно

- Использование `.env` файла для хранения настроек и секретной информации
- Использование [Flatpages](https://docs.djangoproject.com/en/4.0/ref/contrib/flatpages/ "Простые страницы") для статичных страниц
- Добавлен WYSIWYG-редактор [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor) для редактирования Flatpages в интерфейсе администрирования (с переопределением класса `FlatPageAdmin`)
- Использование [наследования моделей](https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes)
- Создана [команда](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/ "Custom django-admin command") для генерирования случайных постов и комментариев к ним для тестирования с использованием библиотек [Factory Boy](https://factoryboy.readthedocs.io/) и [Faker](https://faker.readthedocs.io/en/master/)   

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.2
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.19.2 - Считывает пары ключ-значение из файла .env и может устанавливать их в качестве переменных среды
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) v. 6.2.0
- [factory-boy](https://factoryboy.readthedocs.io/) v. 3.2.1  

## Использованные технологии и программы

- Git, [GitHub](https://github.com/zelo78/), [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)

## TODO

- Полный переход на Class-Based Views
- Использование permissions
- Использование bootstrap 5
- Изменение дизайна страницы
- header и footer в шаблонах
- Кеширование
- Переход на Postgresql 
- Авторизация через социальные сети
- Фильтрация и пагинация в списке постов
- Текстовый поиск в постах
- robots.txt, sitemap.xml
- django-constance
- DRF, создание API
- описание по OpenAPI
- настройка страницы администрирования: фильтрация постов
- кастомная команда опубликовать на странице администрирования постов
