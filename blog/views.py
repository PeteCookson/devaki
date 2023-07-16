# from django.views import generic
# from .models import Post

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

class BlogDetail(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="blog/blog.html", context={"register_form":form})
