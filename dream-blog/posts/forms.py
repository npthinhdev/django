from django import forms
from tinymce import TinyMCE
from .models import Comment, Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={
                'required': False,
                'cols': 30,
                'rows': 10
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content',
                  'thumbnail', 'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'usercomment',
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Type your comment'
            })
        }
        labels = {
            'content': ''
        }
