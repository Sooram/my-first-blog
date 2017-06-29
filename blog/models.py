from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200)
    image= models.ImageField(upload_to='uploads/', blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta: 
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return "/categories/%s/" % self.slug

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey('Post')
    created_date = models.DateTimeField(
            default=timezone.now)

    def __unicode__(self):
        return '%s' % self.author
