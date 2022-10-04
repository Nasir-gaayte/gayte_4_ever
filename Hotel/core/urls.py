from django.urls import path
from core import views
from core.views import AddPost,PostDetail,HomeView,UpdatePost,CommentView


urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='index'),
    path('about/',views.about,name='about'),
    path('team/',views.team,name='team'),
    # path('add_post/',views.add_post,name='add_post'),
    path('add_post/',views.AddPost.as_view(),name='add_post'),
    # path('details/<int:pk>/',views.details,name='details'),
    path('details/<int:pk>/',views.PostDetail.as_view(),name='details'),
    path('update_post/<int:pk>/',views.UpdatePost.as_view(),name='update_post'),
    path('delete_post/<int:pk>/',views.DeletePost.as_view(),name='delete_post'),
    path('comment/<int:pk>/',views.CommentView.as_view(),name='comment'),
]

