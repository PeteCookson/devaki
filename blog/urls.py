# from django.contrib import admin
# from django.urls import path
# from blog import views #here 

# urlpatterns = [
#     path('', views.PostList.as_view(), name='blog'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# ]
from django.contrib import admin
from django.urls import path
from blog import views #here 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog, name='blog'), #here 
]