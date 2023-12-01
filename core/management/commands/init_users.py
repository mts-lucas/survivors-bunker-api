from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Profile
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with fake data for the Profile model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):  # Adapte conforme necessário para o número desejado de perfis
            # Crie um usuário fake ou obtenha um usuário existente
            user, created = User.objects.get_or_create(
                username=fake.user_name(),
                email=fake.email(),
                defaults={'password': fake.password()},
            )

           
            if not created:
                continue

        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))

