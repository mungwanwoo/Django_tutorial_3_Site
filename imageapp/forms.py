from django import forms
from .models import ImagePost

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image', 'description']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'제목을 입력하세요'
            }),
            'image':forms.FileInput(
                attrs={'class':'form-control',}
            ),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'rows':5,
                'placeholder':'이미지의 설명을 입력하세요'
            })
        }