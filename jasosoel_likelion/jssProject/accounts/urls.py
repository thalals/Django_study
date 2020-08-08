from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('signup/', signup, name="signup"),
    #함수 명 대신 클래스 -> as_view를 사용함으로써 url에서 바로실행
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

#login.html 을 registration 폴더에서 빼기위해선 오버라이딩을 해주어야함