from rest_framework import serializers
from .models import Genre, Episode, Anime


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'release_date', 'img_url', 'video']

class AnimeSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    episodes = serializers.IntegerField(source='episodes.count', read_only=True)

    class Meta:
        model = Anime
        fields = ['id', 'title', 'genres', 'status', 'img', 'episodes', 'slug']

class AnimeDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)


    class Meta:
        model = Anime
        fields = ['id', 'title', 'genres', 'status', 'img', 'release_date', 'episodes', 'slug']
