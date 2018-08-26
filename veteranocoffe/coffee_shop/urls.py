from django.urls import path, include
from .views import (
    HomeView,
    NewsListView,
    ContactsView,
    PublicationsListView,
    PublicationsIncludeListView
)

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('news/', NewsListView.as_view(), name = 'news'),
    path('contacts/', ContactsView.as_view(), name = 'contacts'),
    path('publications/', PublicationsListView.as_view(), name = 'publications'),
    path('publications_include/', PublicationsIncludeListView.as_view(), name = 'publications_include')
]