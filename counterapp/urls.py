from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('increment', views.increment, name='increment'),
    path('decrement', views.decrement, name='decrement'),
    path('reset', views.reset, name='reset'),

]
