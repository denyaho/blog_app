from django.urls import path
from blog import views

urlpatterns=[
    path("",views.index),
    path("tags/<slug:slug>/",views.tags),
    path("<slug:pk>/",views.article), #blogの下に出てくる文字をpkに入れる

#    path("/test/",views.test),
]