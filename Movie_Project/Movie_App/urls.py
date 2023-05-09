
from django.urls import path
from . import views
app_name="Movie_App"

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.Update,name='Update'),
    path('delete/<int:id>/',views.Delete,name='Delete')
]
