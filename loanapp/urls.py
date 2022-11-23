from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views as core_views
from core.views import Index, Signup
urlpatterns = [
    path('', core_views.home, name='home'),
    path("login/", auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('Signup', Signup.as_view(), name='Signup'),
    path('index/', Index.as_view(),name='Index'),
   # path('show/', Show.as_view(), name='show'),
    

]