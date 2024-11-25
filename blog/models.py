from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
## modelsはSQLのデータベースを作成できる

class Tag(models.Model):
    slug = models.CharField(primary_key= True,unique=True,max_length=20)#unique→テーブル上で一意な値を持つことを示す
    #primary_key→主キーを設定する
    name = models.CharField(unique=True,max_length=20)

    def __str__(self):
        return self.slug
class Article(models.Model):
    title = models.CharField(default="",max_length=30)#Article→テーブル名,title→列名

    test= models.CharField(default="",max_length=30)

    author=models.CharField(default="",max_length=30)
    created_at = models.DateField(auto_now_add=True)#データが作成されたときに一度だけ日付を入力
    updated_at = models.DateField(auto_now=True)#アップデートされた場合、毎回日付を入力 列名ができた

    count = models.IntegerField(default=0)#整数型のデータを入れる

    tags = models.ManyToManyField(Tag,blank=True)
    #多対多の関係を持つ
    #blank=True→空白を許可する


class Comment(models.Model):
    comment = models.TextField(default="",max_length=500)

    created_at = models.DateField(auto_now_add=True)#初めて作成された時の日時を登録する
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)#
    #on_delete -> 関連先のオブジェクトが削除された時に自身のレコードも削除する

    article= models.ForeignKey(Article,on_delete=models.CASCADE)


