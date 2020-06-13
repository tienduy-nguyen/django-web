from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Post, Category
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView


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
    context_object_name = 'post'


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
