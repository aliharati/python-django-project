import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'mysite.settings')

import django
django.setup()

import random

from polls.models import *
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        #create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name = fake_name)[0]
        access = AccessRecord.objects.get_or_create(name=webpg,date =fake_date)[0]


if __name__ == "__main__":
    print("Populating Scripts!")
    populate(30)
    print("Populating complete!")