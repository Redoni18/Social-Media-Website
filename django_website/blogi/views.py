from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Post, Comment
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils.safestring import SafeString
# Create your views here.


def homepage(request):
    postet = Post.objects.get(public = True).order_by('-koha_posti')
    return render(request,"blogi/home.html",{"Posti":postet})

class PostListView(ListView):
    model = Post
    template_name = 'blogi/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Posti'
    ordering = ['-koha_posti']
    paginate_by = 20


def post_search(request):
    query = request.GET.get('q')
    if(query):
        rezultatet = Post.objects.filter(Q(titulli__icontains = query)|Q(pershkrimi__icontains = query))
    elif(query==''):
        return redirect('home')
    else:
        return redirect('home')
    return render(request,"blogi/search.html",{'search':rezultatet})


class postDetailView(DetailView):
    is_liked = False
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]
        if(post.likes.filter(id=self.request.user.id).exists()):
            context["is_liked"] = True
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulli', 'pershkrimi','foto','foto2','videofile']

    def form_valid(self, form):
        form.instance.autori = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulli', 'pershkrimi','foto','foto2','videofile']

    def post_form_valid(self, form):
        form.instance.autori = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.autori):
            return True
        return False

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.autori):
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'blogi/users_profiles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(autori=user).order_by('-koha_posti')


@login_required(redirect_field_name='home/home.html')
def like(request, pk):
    post = get_object_or_404(Post,  id=pk)
    is_liked = False
    if(post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return redirect('/detail/' + str(post.id))

    

    return render(request,"blogi/post_detail.html",{"Posti":post,'is_liked':is_liked})


@login_required(redirect_field_name='home/home.html')
def comment(request, pk):
    post = get_object_or_404(Post,  id=pk)
    comments = Comment.objects.filter(post=post).order_by('-koha_comment')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comment_autori = request.user
            comment.post = post
            comment.save()
            username = form.cleaned_data.get('emri')
            messages.success(request, f'Comment added successfuly')
            return redirect('/detail/' + str(post.id))
    else:
        form = CommentForm()

    context = {
        "form":form
    }
    
    return render(request,"blogi/comments.html",context)

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if(self.request.user == post.comment_autori):
            return True
        return False


class UpdateCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    labels = {
        "comment": "Write a comment",
        "photo": "Add a photo"
        }
    fields = ['comment','photo']
    success_url = '/'

    def post_form_valid(self, form):
        form.instance.comment_autori = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.comment_autori):
            return True
        return False


def get_likes(request, pk):
    post = get_object_or_404(Post,  id=pk)
    post_likes = post.likes.all()
    print(post_likes)

    return render(request,"blogi/post_likes.html",{'post_likes':post_likes})
