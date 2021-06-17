from django import forms
from .models import Post

class createajax(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content','category']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','id':'titleid'}),
            'author':forms.TextInput(attrs={'class':'form-control','id':'authorid'}),
            'content':forms.TextInput(attrs={'class':'form-control','id':'contentid'}),
            'category':forms.TextInput(attrs={'class':'form-control','id':'categoryid'}),
        }
