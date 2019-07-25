from django import forms
from blog.models import Blog


class BlogForm(forms.ModelForm):
    Blog=forms.CharField(widget=forms.TextInput()
    )
    class Meta:
        model=Blog
        fields=(
            'Heading',
            'Picture',
            'Blog',
            'caption',
            'type',
        )

class BlogEditForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields=(
           'Heading',
           'Picture',
           'Blog',
           'caption',
           'type',
        )