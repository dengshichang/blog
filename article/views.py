from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args) - 1]
    str = ("title = %s, date_time = %s, content = %s"
        % (post.title, post.create_time, post.content))
    return HttpResponse(str)