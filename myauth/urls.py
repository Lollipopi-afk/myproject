from django.urls import path
from .views import logout_view, AboutMeView, RegisterView, login_view

app_name = "myauth"
urlpatterns = [
    # path("login/", login_view, name='login'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("about-me", AboutMeView.as_view(), name='about-me'),
    path("register", RegisterView.as_view(), name='register'),

]