from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article,Comment,Tag
from blog.forms import CommentForm

from django.core.paginator import Paginator
# Create your views here.

def index(request):
    objs=Article.objects.all()
    paginator = Paginator(objs,2)#objの集まりを渡す。２は１ページに表示する記事の上限
    page_number = request.GET.get("page")
    #"page"というクエリがあればその値をとる
    context={
        "page_title": "ブログ一覧",
        "page_obj": paginator.get_page(page_number),
        "page_number": page_number,
    }

    return render(request,"blog/blogs.html",context)

def article(request,pk):
    obj = Article.objects.get(pk=pk)    
    
    if request.method == "POST":
        if request.POST.get("like_count",None):
            obj.count += 1
            obj.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.article = obj
                comment.save()
    comments = Comment.objects.filter(article=obj)
    context={
        "article": obj,
        "comments": comments
    }
    return render(request,"blog/article.html",context)

def text(request):
    return HttpResponse("Hello World")


def tags(request,slug):
    tag = Tag.objects.get(slug=slug)
    articles = tag.article_set.all()#article_setはArticleのインスタンスを取得する
    

    paginator = Paginator(articles,10)#objの集まりを渡す。２は１ページに表示する記事の上限
    page_number = request.GET.get("page")
    #"page"というクエリがあればその値をとる
    context={
        "page_title": f"タグ [{tag.name}] の記事一覧",
        "page_obj": paginator.get_page(page_number),
        "page_number": page_number,
    }

    return render(request, "blog/blogs.html",context)