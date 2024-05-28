from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=40)
    discription=models.CharField(max_length=200,default='')
    publishdate=models.DateField()
    image=models.ImageField(upload_to='shop/images',default='')

    def __str__(self) -> str:
        return self.product_name