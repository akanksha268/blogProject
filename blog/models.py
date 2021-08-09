from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    blog_pic = models.ImageField(upload_to="blog_pics", blank=True)
    stars = models.ManyToManyField(User, default=63)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def star_count(self):
        return self.stars.count()




class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
