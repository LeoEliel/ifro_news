from django.urls import path
from . import views

urlpatterns = {
    path('', views.NewListView.as_view(), name='listarNews'),
    path('cadastrar/', views.NewCreateView.as_view(), name='cadNews'),
}