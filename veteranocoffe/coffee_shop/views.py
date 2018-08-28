from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Publication, Company


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all().order_by('-pub_date')[:3]
        context['publications_list'] = Publication.objects.all().order_by('-pub_date')[:5]
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
    paginate_by = 10
    context_object_name = 'news_list'
    queryset = News.objects.all().order_by('-pub_date')

class PublicationsListView(ListView):
    template_name = 'publications.html'
    model = Publication
    paginate_by = 10
    context_object_name = 'publications_list'
    queryset = Publication.objects.all().order_by('-pub_date')
  
class NewsDetailView(DetailView):
    template_name = 'detail_news.html'
    model = News

class PublicationDetailView(DetailView):
    template_name = 'detail_publication.html'
    model = Publication
