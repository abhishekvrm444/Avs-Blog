import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


def create_post(N):
    fake = Faker()
    for _ in range(N):
        id = random.choice([1,2,3,4,5])
        title = fake.name()
        Post.objects.create(title=title + " Post!!!",
        author = User.objects.get(id=id),
        slug = "-".join(title.lower().split()),
        body = fake.text(),
        created = timezone.now(),
        updated = timezone.now(),
        status='published',
        )



create_post(10)
print("DATA IS POPULATED SUCCESSFULLY.")
