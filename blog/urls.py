from django.urls import path
from . import views

urlpatterns = [
    # CBV방식
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # FBV방식
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index)
]
