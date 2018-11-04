from django.urls import path, include
from . import views

app_name = 'sermons'

urlpatterns = [
	# /sermons/
    path('', views.index, name='index'),
    # /sermons/1 where number is id
    path('<int:pk>/', views.SermonDetailView.as_view(), name='detail'),
    # path('submit.html', views.SubmitSermonView.as_view(), name='submit_sermon'),
]