from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conditii/', views.conditii, name='conditii'),
    path('<int:id_anunt>/', views.anunt, name='detalii-anunt')
]