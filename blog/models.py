# from django.db import models
# from django.contrib.auth.models import User


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils.image_utils import resize_image
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# class Image(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to="images")

#     def __str__(self):
#         return self.image.name

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        # Call the parent's save method
        super().save(*args, **kwargs)

        # Resize the image after it has been saved
        resize_image(self.image)

    def __str__(self):
        return self.image.name
        