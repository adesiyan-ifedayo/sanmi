from django import forms
from django.contrib.auth.models import User
from .models import Contact,Comment


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    username = forms.CharField()
    email = forms.CharField()
    content = forms.CharField(label='',widget=forms.Textarea)


class ContactForm(forms.Form):
    
    name = forms.CharField()
    email = forms.CharField()
    number = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)



class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']    



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)        