from django.urls import path

from .views import RegisterView, LoginView, logout_view


app_name = 'accounts'


urlpatterns = [
    # path("", views.blog_index, name="blog_index"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", logout_view, name="logout"),

]
