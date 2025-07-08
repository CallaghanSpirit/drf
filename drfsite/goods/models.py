from django.db import models


class Goods(models.Model):
    class Status(models.IntegerChoices):
        OUT_OF_STOKE = 0, 'Не в наличии'
        IN_STOCK = 1, 'В наличии'

    name = models.CharField(max_length=255, verbose_name='Имя')
    desc = models.TextField(blank=True)
    cats = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='goods')
    status = models.BooleanField(Status,default=Status.OUT_OF_STOKE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    

    
    def __str__(self):
        
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')

    def __str__(self):
        return self.name
    
    