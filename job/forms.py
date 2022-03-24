from django.forms import ModelForm
from .models import BlogPost

class BlogPostForm(ModelForm):
    '''ModelFormのサブクラス'''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = BlogPost
        fields = ['title', 'content', 'category']
        