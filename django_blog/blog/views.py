from django.shortcuts import render
from django.http import HttpRequest


posts = [
    {
        'author': 'TienDuy',
        'title': 'Blog post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sem sit amet libero condimentum accumsan nec at erat. Quisque egestas felis sit amet ex sodales eleifend. Proin feugiat metus eu rhoncus egestas. Duis tempor magna elit, eget finibus arcu pharetra sed. Vivamus placerat libero ligula, eget dignissim massa dictum vitae. Aliquam finibus vulputate massa, id tincidunt tortor pharetra id. Nunc tempor sem at ante molestie, ac dictum urna eleifend. Aenean sagittis sem sed dui pharetra, vel tristique turpis gravida. Proin fermentum vitae tellus a accumsan. Curabitur quam erat, aliquam id ex ut, mollis faucibus nisl.',
        'date_posted': 'Juin 01, 2020',
        'readtime': '10 min'
    },
    {
        'author': 'TienDuy',
        'title': 'Blog post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sem sit amet libero condimentum accumsan nec at erat. Quisque egestas felis sit amet ex sodales eleifend. Proin feugiat metus eu rhoncus egestas. Duis tempor magna elit, eget finibus arcu pharetra sed. Vivamus placerat libero ligula, eget dignissim massa dictum vitae. Aliquam finibus vulputate massa, id tincidunt tortor pharetra id. Nunc tempor sem at ante molestie, ac dictum urna eleifend. Aenean sagittis sem sed dui pharetra, vel tristique turpis gravida. Proin fermentum vitae tellus a accumsan. Curabitur quam erat, aliquam id ex ut, mollis faucibus nisl.',
        'date_posted': 'Juin 02, 2020',
        'readtime': '5 min'
    },
    {
        'author': 'TienDuy',
        'title': 'Blog post 3',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sem sit amet libero condimentum accumsan nec at erat. Quisque egestas felis sit amet ex sodales eleifend. Proin feugiat metus eu rhoncus egestas. Duis tempor magna elit, eget finibus arcu pharetra sed. Vivamus placerat libero ligula, eget dignissim massa dictum vitae. Aliquam finibus vulputate massa, id tincidunt tortor pharetra id. Nunc tempor sem at ante molestie, ac dictum urna eleifend. Aenean sagittis sem sed dui pharetra, vel tristique turpis gravida. Proin fermentum vitae tellus a accumsan. Curabitur quam erat, aliquam id ex ut, mollis faucibus nisl.',
        'date_posted': 'Juin 03, 2020',
        'readtime': '6 min'
    },
    {
        'author': 'TienDuy',
        'title': 'Blog post 4',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sem sit amet libero condimentum accumsan nec at erat. Quisque egestas felis sit amet ex sodales eleifend. Proin feugiat metus eu rhoncus egestas. Duis tempor magna elit, eget finibus arcu pharetra sed. Vivamus placerat libero ligula, eget dignissim massa dictum vitae. Aliquam finibus vulputate massa, id tincidunt tortor pharetra id. Nunc tempor sem at ante molestie, ac dictum urna eleifend. Aenean sagittis sem sed dui pharetra, vel tristique turpis gravida. Proin fermentum vitae tellus a accumsan. Curabitur quam erat, aliquam id ex ut, mollis faucibus nisl.',
        'date_posted': 'Juin 04, 2020',
        'readtime': '8 min'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
