from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#to create new user
class SignUpForm(UserCreationForm):
	# email = forms.EmailField(label="Email:",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}))
	# first_name = forms.CharField(label="First Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	# last_name = forms.CharField(label="Last Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name','password1','password2']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class']="form-control"
		self.fields['username'].widget.attrs['placeholder']="user name"
		self.fields['username'].widget.label = 'User Name:'
	    
		self.fields['email'].widget.attrs['class']="form-control"
		self.fields['email'].widget.attrs['placeholder']="email"
		self.fields['email'].widget.label = 'Email:'

		self.fields['first_name'].widget.attrs['class']="form-control"
		self.fields['first_name'].widget.attrs['placeholder']="first name"
		self.fields['first_name'].widget.label = 'First Name:'

		self.fields['last_name'].widget.attrs['class']="form-control"
		self.fields['last_name'].widget.attrs['placeholder']="last name"
		self.fields['last_name'].widget.label = 'Password:'
		
		self.fields['password1'].widget.attrs['class']="form-control"
		self.fields['password1'].widget.attrs['placeholder']="password"
		self.fields['password1'].widget.label = 'Retype Password:'
