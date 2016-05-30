from django.conf.urls import url


from .views import (home, carregarImg, simulador)
  
urlpatterns = [  
    url(r'^$', home, name='home'),
    url(r'^carregar-img/$', carregarImg, name='carregar-img'),
    url(r'^simulador/$', simulador, name='simulador'),
]   
    

