import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor.fields import RichTextField #Importamos el CKEditor

def blog_thumbnail_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

def category_thumbnail_path(instance, filename):
    return 'blog_category/{0}/{1}'.format(instance.name, filename)



class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=128)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=category_thumbnail_path, blank=True, null=True)
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name



class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = RichTextField()                                #Agregamos el CKEditor
    thumbnail = models.ImageField(upload_to=blog_thumbnail_path)

    keywords = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)

    status = models.CharField(max_length=10, choices=status_options, default='draft' )

    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager

    category = models.ForeignKey(Category, on_delete=models.PROTECT, )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ("status", "-created_at")

    def __str__(self):
        return self.title
    

class Heading(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='headings')

    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=255)
    lavel = models.IntegerField(
        choices= (
            (1, 'H1'),
            (2, 'H2'),
            (3, 'H3'),
            (4, 'H4'),
            (5, 'H5'),
            (6, 'H6'),
        )
    )

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)