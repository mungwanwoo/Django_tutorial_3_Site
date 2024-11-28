from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_name=models.CharField(max_length=20)
    menu_price=models.IntegerField()
    def __str__(self):
        return self.menu_name

class Option(models.Model):
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    option_name=models.CharField(max_length=20)
    option_price=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.option_name}_{self.option_price}원"