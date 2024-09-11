from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category_name

class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    blog_cover = models.ImageField(upload_to='blog_covers',null=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_date= models.DateField()

    def __str__(self):
        return self.blog_title
    
    
class Comments(models.Model):
    owner = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ('Comments')


# Create your models here.




#Template Inheritance
# {% include 'path' %}