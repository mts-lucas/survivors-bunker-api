from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with fake data for the Profile model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):  # Adapte conforme necessário para o número desejado de perfis
            # Crie um usuário fake
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))
