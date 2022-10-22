from django.shortcuts import render , redirect 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from .forms import ArticleForm , UserCreationForm2
from django.contrib import messages
from django.http import HttpResponse 
from rest_framework import viewsets


def index(request):
    return render (request, 'auth/index.html')


class Registration(CreateView):
    form_class = UserCreationForm2
    success_url = reverse_lazy("index")
    template_name = "registration/registration.html"


def display_articles(request):
    articles = Article.objects.all()
    return render(request,'auth/index.html',{'articles':articles})


def registration(request):
    flash = {'error':[]} # сюда добавить оповещения и т.д.
    form = UserCreationForm2(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return index(request)   
        else:
            flash['error'].append('Пароль должен содержать не менее 8 символов,иметь заглавную букву и символаааа') 
            return render(request,"registration/registration.html",{'form': form, 'flash':flash})
    else:
        return render(request,"registration/registration.html",{'form': form})
   
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def create(request):
    error = {'error':[]}
    sucess = {'sucess':[]}
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        photo = request.FILES.get('file')
        choice = request.POST.get('choice')
        article = Article(title=title,content=content,image=photo,cat_name_id=choice)
        if choice == 'Статья1':
            choice = 1
        elif choice == 'Статья2':
            choice = 2
        elif choice == 'Выберите категорию':
            messages.error(request, 'Invalid form submission')
            if title and content and choice:
                article.save() 


    return render(request, 'auth/create.html', {'sucess':sucess,'error':error})





























    # def create():
    # def __init__(self, *args, **kwargs):
    #     super(Registration, self).__init__(*args, **kwargs)

        
    #     self.fields['username'].widget.attrs['class'] = 'form-control' 
    #     self.fields['password1'].widget.attrs['class'] = 'form-control' 
    #     self.fields['password2'].widget.attrs['class'] = 'form-control' 

# class MyUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = ''
#         self.fields['password'].help_text = ''
    