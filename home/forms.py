from django import forms
from home.models import Post

class PostForm(forms.ModelForm):
    caption=forms.CharField(widget=forms.TextInput(
      attrs={
          'class':'form-control',
          'placeholder':"Write something..."



      }
    ))

    class Meta:
        model=Post
        fields=(
            'Heading',
            'Picture',
            'caption',
        )


