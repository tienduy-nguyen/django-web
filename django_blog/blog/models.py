from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from taggit.managers import TaggableManager
from .utils import unique_slug_generator, get_read_time
from django.db.models.signals import pre_save, post_save
from PIL import Image

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        self.slug = self.slug.lower()
        return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    catetory = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=100, verbose_name="Title")
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(verbose_name="Content")
    tags = TaggableManager()
    author = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE)
    photo_main = models.ImageField(
        default='defaultPost.png', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Create at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    read_time = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at', '-updated_at']

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

     # Scale image before upload
    def save(self, *args, **kwargs):
        self.read_time = get_read_time(self.content)
        super().save()

        img = Image.open(self.photo_main.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo_main.path)


# Create a unique slug
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Post)
