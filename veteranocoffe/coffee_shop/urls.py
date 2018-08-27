from django.urls import path, include
from .views import (
    HomeView,
    NewsListView,
    ContactsView,
    NewsDetailView,
    PublicationDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('news/', NewsListView.as_view(), name = 'news'),
    path('contacts/', ContactsView.as_view(), name = 'contacts'),
    path('news/<pk>/', NewsDetailView.as_view(), name = 'detail_news'),
    path('publication/<pk>/', PublicationDetailView.as_view(), name = 'detail_publication')
]