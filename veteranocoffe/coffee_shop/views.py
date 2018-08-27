from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Publication, Company
from itertools import chain


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = reversed(News.objects.all())
        context['publication_list'] = reversed(Publication.objects.all())
        return context

class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies_list'] = Company.objects.all()
        return context

class NewsListView(ListView):
    template_name = 'news.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_news_list'] = chain(reversed(News.objects.all()), reversed(Publication.objects.all()))
        context['news_list'] = News.objects.all()
        context['publication_list'] = Publication.objects.all()
        return context
  
class NewsDetailView(DetailView):
    template_name = 'detail_news.html'
    model = News

class PublicationDetailView(DetailView):
    template_name = 'detail_publication.html'
    model = Publication
