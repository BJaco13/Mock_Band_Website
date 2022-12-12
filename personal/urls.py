from django.urls import path, include
from . import views
from django.views.generic import ListView
from .models import Shows
from .views import ShowsListView

urlpatterns = [
path('', views.index, name = 'index'),
path('products/', views.products, name = 'products'),
path('about_me/', views.about_me, name = 'about_me'),
path('shows/',ListView.as_view(
queryset=
Shows.objects.all().order_by("date")[:25],
template_name="display.html"), name = 'shows'),


path('login/', views.user_login, name='login'),
path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
path('register_user/', views.register_user, name = 'register_user'),
path('logout/', views.logout_view, name = 'logout'),
path('profile/', views.profile, name = 'profile')
]