from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView, UpdateView,DeleteView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.



def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'travel/home.html',context)  #REMEMBER TO CHANGE TO  render() for HTML

class PostListView(ListView): #to see all the posts in order
    model = post
    template_name = 'travel/home.html'  # <app>/model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # makes the order of the post from newest to oldest.
    paginate_by = 5 #makes pages only two posts per page

class UserListView(ListView): #to see all the posts in order from the user
    model = post
    template_name = 'travel/user_posts.html'  # <app>/model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # makes the order of the post from newest to oldest.
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):  # to see a detailed post when clicked on
    model = post


class PostCreateView(LoginRequiredMixin,CreateView): # lets us create a new post, the loginRequiredMixin paramater forces us to be logged in order to create a new post
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # need login require and only same user who created post can update a post
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # need login require and user who created post can delete a post
    model = post
    success_url = '/'  #after deleting post it goes back to home page

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


def about(request):
    # return HttpResponse('<h1> Travel About</h1>')
    return render(request, 'travel/about.html', {'title': "About"})