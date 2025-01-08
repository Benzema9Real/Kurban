from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    GenreListCreateView, AnimeListView, AnimeDetailView,
    EpisodeListView, EpisodeDetailView, AnimeSearchView
)

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('anime/', AnimeListView.as_view(), name='anime-list'),
    path('anime/<slug:slug>/', AnimeDetailView.as_view(), name='anime-detail'),
    path('anime/<slug:slug>/episodes/', EpisodeListView.as_view(), name='episode-list'),
    path('anime/<slug:anime_slug>/episodes/<slug:slug>/', EpisodeDetailView.as_view(), name='episode-detail'),
   path('search/', AnimeSearchView.as_view(), name='anime-search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
