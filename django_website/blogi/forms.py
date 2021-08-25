from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget = forms.Textarea, required = False)
	class Meta:
		model = Comment
		labels = {
		"comment": "Write a comment",
		"photo": "Add a photo"
        }
		fields = ['comment','photo']