from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import News, Publication, Company
from itertools import chain


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()
        context['publication_list'] = reversed(Publication.objects.all())
        context['companies_list'] = Company.objects.all()
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
        context['news_list'] = chain(reversed(News.objects.all()), reversed(Publication.objects.all()))
        return context
  


class PublicationsListView(ListView):
    template_name = "publications.html"
    model = Publication


class PublicationsIncludeListView(ListView):
    template_name = "publications_include.html"
    model = Publication
