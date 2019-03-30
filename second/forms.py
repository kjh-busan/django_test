from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='제목', max_length=200)
    content = forms.CharField(label='내용', widget=forms.Textarea)