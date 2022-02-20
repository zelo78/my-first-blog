import random
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import User
from factory import Faker, fuzzy, LazyFunction
from factory.django import DjangoModelFactory

from blog.models import Post, Comment


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = LazyFunction(lambda: random.choice(User.objects.all()))
    title = Faker('sentence', nb_words=4, locale='ru_RU')
    text = Faker('paragraph', nb_sentences=6, locale='ru_RU')
    published_date = fuzzy.FuzzyDateTime(start_dt=timezone.now()-timedelta(days=730))


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    post = LazyFunction(lambda: random.choice(Post.objects.all()))
    author = Faker('name', locale='ru_RU')
    text = Faker('paragraph', nb_sentences=4, locale='ru_RU')
    approved_comment = Faker('pybool')
