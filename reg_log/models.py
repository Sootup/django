from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    cat_name = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.cat_name

class Article(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=50,blank=False)
    content = models.CharField(max_length=255,blank=False)
    image = models.ImageField(upload_to='img/%Y/%m/%d/',default=None,blank=True)
    creation_date = models.DateField(auto_now_add=True)
    last_change = models.DateField(auto_now=True,blank=True)
    cat_name = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

