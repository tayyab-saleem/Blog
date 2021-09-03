from django import forms
from django.forms import widgets
from django.forms.widgets import HiddenInput
from .models import Blog, Comment

# class DashBoardForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields =('title','dsc',)
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'container'}),
#             'dsc': forms.Textarea(attrs={'class':'container '}),
#         }

class Edit_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields =('title','dsc')
        widgets = {
            'title': forms.TextInput(attrs={'class':'container'}),
            'dsc': forms.Textarea(attrs={'class':'container '}),
        }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)

        widgets = {
            
            'body': forms.Textarea(attrs={'class':'form-control '}),
        }





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)

        widgets = {
            
            'body': forms.Textarea(attrs={'class':'form-control '}),
        }

class New_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields =('title', 'dsc', 'user_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].disabled = True    
