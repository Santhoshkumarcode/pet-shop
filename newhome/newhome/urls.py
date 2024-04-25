from django.contrib import admin
from django.urls import path
from petapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.reg,name='register'),
    path('login/',views.log,name='login'),
    path('landing/',views.landing,name='landing'),
    path('adopt/',views.adopt,name='adopt'),
    path('donate/',views.donate,name='donate'),
    path('buy/',views.buy,name='buy'),
    path('result/',views.result,name='result'),
    path('cat/',views.cat,name='cat'),
    path('dog/',views.dog,name='dog'),
    path('catbuy',views.catbuy,name='catbuy'),

]
