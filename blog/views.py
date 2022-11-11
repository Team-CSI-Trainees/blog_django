from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Post_image,Message
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home(request):
    q=request.GET.get('q') if request .GET.get('q')!=None else ''
    posts=Post.objects.filter(Q(author__username__icontains=q)|Q(content__icontains=q)|Q(title__icontains=q))
    post_count=posts.count()
    context = {
        'posts':posts,
        'post_count':post_count
    }
    paginate_by=5
    return render(request, 'blog/home.html', context)
def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    post_messages=post.message_set.all().order_by('-created')
    if request.method == 'POST':
        message=Message.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        return redirect('post-detail',pk=post.id)
    context={'post':post,'post_messages':post_messages}

    return render(request,"blog/post_detail.html",context)
@login_required
def deletemessage(request,pk):
    message=Message.objects.get(id=pk)
    if request.user!=message.user :
        return HttpResponse("You are not allowed to do it.")
    if request.method=='POST':
        message.delete()
        return redirect('post-detail',pk=message.post.id)
    return render(request,'blog/delete_msg.html',{'message':message})


# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
  

class PostUserView(ListView):
    model = Post
    template_name = 'blog/singleuser.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
   
    #def get_queryset(self):
        #user=get_object_or_404(User , username=self.kwargs.get('username'))
        #return Post.objects.filter(author=user).order_by('date_posted')


# class PostDetailView(DetailView):
#     model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class Postimage(LoginRequiredMixin, CreateView):
    model = Post_image
    fields = ['image']
    template_name = 'blog/post_image.html'

    def form_valid(self, form):
        form.instance.author = self.request.post
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
