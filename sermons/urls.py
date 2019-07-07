from . import views
from django.urls import path


app_name = 'sermons'

urlpatterns = [
    # /sermons/
    path('', views.index, name='index'),
    # /sermons/1 where number is id
    path('<int:pk>/', views.SermonDetailView.as_view(), name='detail'),
]
