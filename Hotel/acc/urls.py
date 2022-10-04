from django.urls import path
from acc import views


urlpatterns = [
    path('login/',views.login_req,name='login'),
    path('logout/',views.logout_req,name='logout'),
]
