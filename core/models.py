from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/%Y/%m/%d/', blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nickname}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Survivor(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='survivors')
    author_comment = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='survivors/%Y/%m/%d/', blank=True, null=True, default='')
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
        return f'survivor {self.name}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Survivor'
        verbose_name_plural = 'Survivors'

class Monster(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='monsters')
    author_comment = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='monsters/%Y/%m/%d/', blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    characteristics = models.TextField()
    remaining_torments = models.TextField(null=True, blank=True)
    conditions = models.TextField()

    def __str__(self) -> str:
        return f'monster {self.name}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'
