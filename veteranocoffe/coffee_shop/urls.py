from django.urls import path, include
from .views import (
    HomeView,
    NewsListView,
    PublicationsListView,
    ContactsView,
    NewsDetailView,
    PublicationDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('news/', NewsListView.as_view(), name = 'news'),
    path('publications/', PublicationsListView.as_view(), name = 'publications'),
    path('contacts/', ContactsView.as_view(), name = 'contacts'),
    path('news/<pk>/', NewsDetailView.as_view(), name = 'detail_news'),
    path('publications/<pk>/', PublicationDetailView.as_view(), name = 'detail_publication')
]