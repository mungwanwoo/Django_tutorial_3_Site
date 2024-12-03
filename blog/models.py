from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name='카테고리')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='생성일')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='카테고리'
        verbose_name_plural='카테고리 목록'
        db_table='mgw_category'
        ordering=['name']



class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name= '작성자')
    # author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name= '작성자')
    title = models.CharField(max_length=200,verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='카테고리')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='작성일')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='게시글'
        verbose_name_plural='게시글 목록'
        db_table='mgw_post'
        ordering=['-create_at']
        indexes = [
            models.Index(fields=['-create_at'])
        ]
