import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'second_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        mail = fakegen.email()

        user = User.objects.get_or_create(firstName = fname, lastName =lname,email=mail)[0]
        
if __name__ == "__main__":

    populate(30)