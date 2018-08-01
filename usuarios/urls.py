from django.urls import path, include
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.do_login, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.do_login, name='login'),
    path('logout', views.do_logout, name='logout'),
    path('perfil', views.perfil, name='perfil'),
    path('character/new/', views.create_character, name='create_character'),
    path('character/edit/<int:id>/', views.update_character, name='update_character'),
    path('character/delete/<int:id>/', views.delete_character, name='delete_character'),
    path('event/search/<int:id>/', views.search_event, name='search_event'),
    path('event/edit/<int:id>/', views.edit_event, name='edit_event'),
    path('guild/new', views.create_guild, name='create_guild')
]