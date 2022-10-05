from .models import Post
from django.views.generic import ListView, DetailView

class NewsList(ListView):
    model = Post
    ordering = '-data_time'
    template_name = 'news.html'
    context_object_name = 'news'

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

# Create your views here.
