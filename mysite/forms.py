from django import forms
from django.contrib.auth import get_user_model #setting.pyのAUTH_USER_MODELで指定したモデルを呼び出す
from mysite.models.profile_models import Profile

class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
 
    class Meta:
        model = get_user_model()
        fields = ('email',)
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
 
    def save(self, commit=True):
        user = super().save(commit=False)
        ##ModelFormのsaveメソッドを呼び出し、commit=Falseにして保存しないようにする
        ## ユーザーオブジェクトは作成されるが、データベースに保存されない
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username' ,
            'zipcode',
            'prefecture',
            'city',
            'address',
            'images',
        )#Modelから上記変数を受け入れる
 
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user