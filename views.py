from django.shortcuts import render
from.models import Post,Category,Author
from django.views.generic import DetailView


def news(request):
    news = Post.objects.order_by('dateCreation')
    return render(request,'news_portal/news.html',{'news':news})

class NewsDetail(DetailView):
   model = Post
   template_name = 'news_portal/details_view.html'
   context_object_name = 'post'


