# your_app/management/commands/populate_survivors.py
from random import randint

from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Profile, Survivor


class Command(BaseCommand):
    help = 'Populate the database with fake data for the Survivor model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):  # Ajuste conforme necessário para o número desejado de sobreviventes
            # Crie um usuário fake
            myuser = User.objects.get(pk=randint(1,50))

            # Crie um perfil fake
            profile = Profile.objects.get(user=myuser.id)

            # Crie um sobrevivente fake
            survivor = Survivor.objects.create(
                author=profile,
                author_comment=fake.text(),
                name=fake.name(),
                codename=fake.user_name(),
                characteristics=fake.text(),
                torments=fake.text(),
                conviction=fake.random_int(min=1, max=12),
                conditions=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))
