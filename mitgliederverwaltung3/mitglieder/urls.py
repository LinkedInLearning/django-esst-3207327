from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:mitgliedsnr>/', views.delete, name='delete'),
    path('update/<int:mitgliedsnr>', views.update, name='update'),
    path('update/updaterecord/<int:mitgliedsnr>', views.updaterecord, name='updaterecord'),
]