
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,TextInput, ImageField, ClearableFileInput, Textarea, PasswordInput,CharField, FileInput ,Select, MultipleChoiceField
from .models import Article, Category
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import password_validation


# class MyUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = 'Введите логин'
#         self.fields['password'].help_text = 'Введите пароль'

class UserCreationForm2(UserCreationForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] ='Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] ='Подтвердите пароль'
        self.fields['username'].widget.attrs['placeholder'] ='Введите логин'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2


    # def save(self, commit=True):
    #     user = super(UserCreationForm2,self).save(commit=False)
    #     if commit:
    #         user.save()
    #     return user
    
    
    
    # password1 = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password",place}),
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
    # )







# class RegistrationForm(ModelForm):
#     class Meta:
#         model = Registration
#         fields = ['username','password1','password2']

#         widgets = {
#             'username' : CharField(attrs={'class':'form-control','placeholder':'Введите логин'}),
#             'password1' : PasswordInput(attrs={'class':'form-control','placeholder':'Введите пароль'}),
#             'passwrod2': PasswordInput(attrs={'class':'form-control','placeholder':'Потвердите пароль'})
#         }


def get_category():
    category = Category.objects.all().values()
    choice = []
    for cat in category:
        for k,v in cat.items():
            choice.append([k,v])
    print(choice)
    return choice


class ArticleForm(forms.Form):
    choice = get_category()
    # title = forms.CharField()
    # content = forms.Textarea()
    # image = forms.ClearableFileInput()
    cat_name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choice)

    
    # attrs={'class':'form-control','placeholder':'Введите название статьи'}
    # attrs={'class':'form-control','placeholder':'Содержание Статьи'}


    # 'ChoiceField', 'MultipleChoiceField',
    # 'ComboField', 'MultiValueField',
    # 'TypedChoiceField', 'TypedMultipleChoiceField'




    # class Meta:
    #     model = Article
    #     fields = ['title','content','image','id_cat']
    #     options = get_category()
    #     widgets = {
    #         "title": TextInput(attrs={'class':'form-control','placeholder':'Введите название статьи'}),
    #         "content": Textarea(attrs={'class':'form-control','placeholder':'Содержание Статьи'}),
    #         "image": ClearableFileInput(),
    #         "id_cat": MultipleChoiceField(choices=options
    #     }