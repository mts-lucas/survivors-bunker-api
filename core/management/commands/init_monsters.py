# your_app/management/commands/populate_Monsters.py
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Profile, Monster


class Command(BaseCommand):
    help = 'Populate the database with fake data for the Monster model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):  # Ajuste conforme necessário para o número desejado de sobreviventes
            # Crie um usuário fake
            myuser = User.objects.get(pk=1)

            # Crie um perfil fake
            profile = Profile.objects.get(user=myuser.id)

            # Crie um sobrevivente fake
            monster = Monster.objects.create(
                author=profile,
                author_comment=fake.text(),
                name=fake.name(),
                characteristics=fake.text(),
                remaining_torments=fake.text(),
                conditions=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))