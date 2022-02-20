import random

from django.core.management.base import BaseCommand

from blog import models, factories


class Command(BaseCommand):
    help = 'Populate DB with a few posts for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=40, type=int, help='Count of posts to be created, default 40')

    def handle(self, *args, **options):
        count = options['count']

        # мы добавим count опубликованных постов
        for i in range(count):
            post = factories.PostFactory.create()
            comments_count = random.randint(0, 5)
            if comments_count > 0:
                factories.CommentFactory.create_batch(comments_count, post=post)

        # добавляем несколько неопубликованных постов
        # у них не будет комментариев
        unpublished_count = 1 + count // 10
        factories.PostFactory.create_batch(unpublished_count, published_date=None)
