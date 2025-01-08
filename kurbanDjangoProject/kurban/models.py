from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
def validate_mp4(file):
    if not file.name.endswith('.mp4'):
        raise ValidationError('Файл должен быть в формате MP4.')

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Anime(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='anime')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    release_date = models.DateField()
    img = models.URLField(blank=True, null=True)
    episodes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Episode(models.Model):
    anime = models.ForeignKey(Anime, related_name='anime_episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    img_url = models.URLField(blank=True, null=True)
    video = models.FileField(upload_to='episode_videos/', null=True, blank=True, validators=[validate_mp4])
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.anime.title} - {self.title}"
