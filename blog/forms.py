from django import forms
from .models import Post, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'카테고리명을 입력하세요'
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','category','content']
        widgets = {
            'author':forms.Select(attrs={
                'class':'form-control',
                
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'제목을 입력하세요'
            }),
            'category':forms.Select(attrs={
                'class':'form-control',
            }),
            'content':forms.TextInput(attrs={
                'class':'form-control',
                'rows':10,
                'placeholder':'내용을 입력하세요'
            })
        }