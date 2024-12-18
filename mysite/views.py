from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm,ProfileForm
from django.contrib import messages

import os
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required  
from django.contrib.auth import login

def index(request):
    ranks = Article.objects.order_by("-count")[:2] #countの降順に並べる

    objs = Article.objects.all()[:3]
    context={
        "title": "Really Site",
        "articles": objs,
        "ranks": ranks,
    }##keyを使ってvalueをテンプレートの中で使える(値を渡せる)

    return render(request,"mysite/index.html",context)
    return HttpResponse("Hello Really Site")

# def login(request):
#     context={}
#     if request.method == "POST":
#         context["req"]= request.POST
#     return render(request,"mysite/login.html",context)

class Login(LoginView):
    template_name="mysite/auth.html"

    def form_valid(self,form):
        messages.success(self.request,"ログイン完了!!")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"ログイン失敗")
        return super().form_invalid(form)

def signup(request):
    context={}
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#saveするけど、データベースには保存しない
#            user.is_active = False
            user.save()
            login(request,user)##ログインする
            messages.success(request, "登録完了!")
            return redirect("/")
    return render(request,"mysite/auth.html",context)


@login_required
def mypage(request):    
    context = {}
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():##エラーかどうかを確認
            profile = form.save(commit=False) #中身をprofile変数として保存する
            profile.user = request.user
            profile.save()
            messages.success(request,"プロフィールを更新しました")
            return redirect("/mypage")
    return render(request,"mysite/mypage.html",context)



def contact(request):
    context = {
        "grecaptcha_sitekey": os.environ["GRECAPTCHA_SITEKEY"],
    }
    if request.method == "POST":
        recaptcha_token = request.POST.get("g-recaptcha-response")
        res = grecapthca_request(recaptcha_token)
        if not res:
            messages.error(request,"reCAPTCHAエラー")
            return render(request,"mysite/contact.html",context)
        
    # if request.method == "POST":
    #     subject = "お問い合わせがありました"
    #     message = """お問い合わせがありました\n 
    #     名前: {} \n 
    #     メールアドレス: {} \n 
    #     お問い合わせ内容: {}""".format(request.POST.get("name"),request.POST.get("email"),request.POST.get("content"))

    #     email_from = os.environ["DEFAULT_EMAIL_FROM"]
    #     emaiil_to = [os.environ["DEFAULT_EMAIL_FROM"],]
    #     send_mail(subject,message,email_from,emaiil_to)

    return render(request,"mysite/contact.html",context)

def grecapthca_request(token):
    from urllib import request,parse
    import json,ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    url = "https://www.google.com/recaptcha/api/siteverify"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {
        "secret": os.getenv("GRECAPTCHA_SECRET"),
        "response": token,
    }

    data = parse.urlencode(data).encode()
    req = request.Request(
        url,
        method="POST",
        headers=headers,
        data=data,
    )

    f= request.urlopen(req,context=context)
    response = json.loads(f.read())
    f.close()

    print("-----")
    print(response)
    return response["success"]
