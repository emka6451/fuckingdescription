from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Image = models.ImageField()
    Content = RichTextUploadingField(config_name='default')
    Tag = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=200, unique=True)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    def __unicode__(self):
        return u'%s' % self.Title
    
    class Meta:
        ordering = ('-Date',)


class Comment(models.Model):
    Post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Body = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=True)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null= True, blank=True, related_name='replies')

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return 'Comment By {}'.format(self.Name)

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    start_time = models.CharField(max_length=255 ,default=timezone.now())
    appointment_time = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='event')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='events')

    def __str__(self):
        return self.name
