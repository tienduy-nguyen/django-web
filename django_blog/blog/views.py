from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, Http404, HttpResponseNotFound
from django.db.models import Q
from .models import Post, Category
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts
    }
    if request.user.is_authenticated:
        return render(request, 'blog/posts/postList.html', context)
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts/postList.html'
    context_object_name = 'posts'
    ordering = ['-created_at', '-updated_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/posts/postDetail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    # redirect_field_name = 'next'
    model = Post
    fields = ['catetory', 'title', 'slug', 'content', 'tags',
              'photo_main', 'is_published']
    template_name = 'blog/posts/postCreate.html'
    # context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/accounts/login/'
    # redirect_field_name = 'next'
    model = Post
    fields = ['catetory', 'title', 'slug', 'content', 'tags',
              'photo_main', 'is_published']
    template_name = 'blog/posts/postCreate.html'
    # context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/posts/postDetail.html', context)


def about(request):
    return render(request, 'blog/about.html')


def categoryList(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog/category/categoryList.html', context)


def categoryDetail(request, slug):
    categories = Category.objects.all()
    posts = Post.objects.filter(is_published=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        postList = posts.filter(category=category)
        context = {
            'posts': postList
        }
    return render(request, 'blog/category/categoryDetail.html', context)

# def tag_list(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'blog/categoryList.html', context)


# def tag_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     context = {
#         'category': category
#     }
#     return render(request, 'blog/categoryDetail.html', context)

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def post_feed(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:  # this is a separate variable (for searching I'm assuming)
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            # I would consider taking this out. It's gonna cause problems.
            Q(tags__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    # bring pagination/tag lookup outside of the if query block -- so you don't NEED a query
    paginator = Paginator(queryset, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "tags": Post.tags.objects.all()[0:20],  # first 20 tags of all tags
        "title": "List",
        "page_request_var": page_request_var,
    }

    return render(request, "post_feed.html", context)


""" modelled after the function above -- so it's easy to understand """


def tag_list(request, tag_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    queryset = Post.objects.filter(tag__id=tag_id)
    paginator = Paginator(queryset, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "tags": Post.tags.objects.all()[0:20],  # first 20 tags of all tags
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "post_feed.html", context)
