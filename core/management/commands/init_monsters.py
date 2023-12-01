# your_app/management/commands/populate_Monsters.py
from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Monster, Profile

class Command(BaseCommand):
    help = 'Populate the database with fake data for the Monster model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):  # Ajuste conforme necessário para o número desejado de sobreviventes
            # Crie um usuário fake
            myuser = User.objects.get(pk=randint(1, 50))

            # Crie um perfil fake
            profile = Profile.objects.get(user=myuser.id)

            # Tente obter um Monster com as mesmas características
            monster, created = Monster.objects.get_or_create(
                author=profile,
                author_comment=fake.text(),
                name=fake.name(),
                characteristics=fake.text(),
                remaining_torments=fake.text(),
                conditions=fake.text(),
            )

            if not created:
                # Se o Monster já existe, não faça nada
                continue

        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))
