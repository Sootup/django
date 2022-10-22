from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('reg', views.registration, name = 'registration'),
    path('create',views.create,name='create'),
    path('api/v1/category/',views.CategoryViewSet.as_view({'get':'list'}),name='apicategory'),
    path('api/v1/article/',views.ArticleViewSet.as_view({'get':'list'}),name='apiarticle')

]
