from django.urls import path
from .views import home, signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   
    path('', home, name='home'),
    path('signup/', signup, name ="signup"),
    path('login/', LoginView.as_view(), name ="login"),
    path('logout/', LogoutView.as_view(), name ="logout"),
]
