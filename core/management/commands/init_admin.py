from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comando para criar o usuário administrador."""

    def handle(self, *args, **options):
        """Implementação da criação do usuário administrador."""

        username = 'admin'
        email = 'admin@example.com'
        password = 'password'
        if not User.objects.filter(username=username).exists():
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password)
            print('The %s account created successfully.' % str(admin))
        else:
            print('Admin account has already been initialized.')
