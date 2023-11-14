from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photos/profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=32)

    def __str__(self):
        return f'{nickname}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Survivor(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='photos/survivors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    codename = models.CharField(max_length=32, blank=True, null=True)
    characteristics = models.TextField()
    torments = models.TextField()
    conviction = models.IntegerField(
        validators=[
            MinValueValidator(1, message='O número deve ser no mínimo 1.'),
            MaxValueValidator(12, message='O número deve ser no máximo 12.'),
        ]
    )
    conditions = models.TextField()

    def __str__(self) -> str:
        return f'survivor {name}'
    
    class Meta:
        verbose_name = 'Survivor'
        verbose_name_plural = 'Survivors'

class Monster(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='photos/survivors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    characteristics = models.TextField()
    remaining_torments = models.TextField(null=True, blank=True)
    conditions = models.TextField()

    def __str__(self) -> str:
        return f'monster {name}'
    
    class Meta:
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'
