from django.shortcuts import render
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by=6 #한 페이지에 몇개씩 출력할 것인지 결정하는 값

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix='_create'

class BookmarkDetailView(DetailView):
    model=Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix='_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
