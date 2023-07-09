# from django.views import generic
# from .models import Post

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})