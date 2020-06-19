from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
# from blog.views import handler404, handler500
from django.conf.urls import(
    handler404, handler500
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('users.urls')),
    path('markdownx/', include('markdownx.urls')),
]

handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
