# from django.contrib import admin
# from django.urls import path
# from blog import views #here 

# urlpatterns = [
#     path('', views.PostList.as_view(), name='blog'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# ]
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_list, name='blog_list'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('register', views.register_request, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)