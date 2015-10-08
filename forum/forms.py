from django import forms

from .models import Thread, Comment

class NewThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields  = ['username', 'title', 'description' ]

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields  = ['content', 'username', 'thread']

    def save(self, commit=True):
        comment = super(NewThreadForm, self).save(commit=False)
        comment.thread.save()
        if commit:
            comment.save()
        return user


