from rest_framework.permissions import AllowAny

# from .filter import AnimeFilter
from .models import Genre, Episode, Anime
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Genre, Anime, Episode
from .serializers import GenreSerializer, AnimeSerializer, EpisodeSerializer, AnimeDetailSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class AnimeListView(generics.ListAPIView):
    serializer_class = AnimeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre = self.request.query_params.get('genre')
        status = self.request.query_params.get('status')

        if genre:
            queryset = queryset.filter(genres__slug=genre)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

class AnimeDetailView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

class EpisodeListView(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class EpisodeDetailView(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Получаем slug из URL, затем фильтруем эпизоды по этому slug из модели Anime
        anime_slug = self.kwargs.get('anime_slug')  # Слаг аниме
        return self.queryset.filter(anime__slug=anime_slug)

# class AnimeSearchView(generics.ListAPIView):
#     queryset = Anime.objects.all()
#     serializer_class = AnimeSerializer
#     permission_classes = [AllowAny]
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = AnimeFilter