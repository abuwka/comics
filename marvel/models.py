from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200,verbose_name='Имя')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.CharField(verbose_name='Имя героя',max_length=200)
    comics = models.TextField(verbose_name='Комикс')
    side = models.CharField(verbose_name='Добро или Зло',max_length=50)
    images = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')


    def __str__(self):
        return self.name

class Post(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

class Comment(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    author_name = models.CharField(verbose_name='Имя автора', max_length=50)
    comment_text = models.CharField(verbose_name='текст комментария', max_length=200)
