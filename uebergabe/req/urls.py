from django.urls import path
from . import views
  
urlpatterns = [
         path('', views.index, name='index'),
         path('para/<int:nr>', views.para, name='para'),
]