from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface, name='interface'),
    path('login', views.login, name='login'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('page2', views.page2, name='page2'),
    path('insert', views.insert, name='insert'),
    path('update/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'),
    path('aboutUs', views.about, name='aboutUs'),
    path('avis', views.avis, name='avis'),
    path('ajoutAvis', views.ajoutAvis, name='ajoutAvis'),
    path('filter',views.filter,name="filter")
]