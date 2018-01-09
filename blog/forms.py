#from django import forms
# class PostForm(forms.Form):
#    content = forms.CharField(max_length=256)
#    created_at = forms.DateTimeField()
    
from django import forms
from .models import Post
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)