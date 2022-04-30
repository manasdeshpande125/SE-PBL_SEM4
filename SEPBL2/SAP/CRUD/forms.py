from django import forms 
from django.contrib.auth.models import User 
from CRUD.models import Achievements,profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class Achievements(forms.ModelForm):  
    title= forms.CharField()
    description=forms.CharField()
    support=forms.CharField()
    certificate=forms.FileField() 
    widgets = {
        'title':forms.TextInput(attrs={
            'class': 'form-control'}),
        'description':forms.TextInput(attrs={
            'class': 'form-control'}),
        'support':forms.TextInput(attrs={
            'class': 'form-control'}),
        'certificate':forms.FileInput(attrs={
            'class': 'form-control-file'})
    }
        
    class Meta:  
        model = Achievements 
        #fields = "__all__"  
        fields=['title', 'description','support','certificate']
class profile(forms.ModelForm):
    class Meta:
        model=profile
        fields = "__all__"
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 550px;'}))

    

    class Meta:
        model = User
        fields = ['username', 'email']

class EditProfileForm(UserChangeForm):
    password=None
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 550px;'}))
    


    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
        help_texts = {
            'username': None,
            'password1':None,
            'password2':None,
        }


class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 550px;'}))
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2','email']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1' ,'password2' ]
        '''help_texts = {
                'username': None,
                'email': None,
                'password1':None,
                'password2':None,
            }'''

    def clean(self):
      super(UserForm, self).clean()

      # getting username and password from cleaned_data
      username = self.cleaned_data.get('username')
      if username[0:4]!='C2K2':
          self._errors['username'] = self.error_class(['Username must start with C2K2,I2K2,E2K2'])





