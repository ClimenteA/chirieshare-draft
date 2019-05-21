from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conditii/', views.conditii, name='conditii'),
    path('detalii-anunt/<int:pk>', views.anunt, name='detalii-anunt')
]