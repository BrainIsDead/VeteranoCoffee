from django.urls import path, include
from .views import HomeView, NewsListView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    #path('', HomeView.as_view(), name = 'home'),
]