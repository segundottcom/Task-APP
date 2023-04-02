from django import forms
from .models import *

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	
	member = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Assigned to:...'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
	class Meta:
		model = task
		fields = ['title', 'member', 'due']
  


class UpdateForm(forms.ModelForm):
		title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

		class Meta:
     
			model = task
			fields = ['title', 'member', 'due', 'complete']