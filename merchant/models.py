from django.db import models

# Create your models here.
class Merchant(models.Model):
    merchant_name = models.CharField(max_length=250)
    merchant_code = models.CharField(max_length=25)
    merchant_address = models.TextField()

    

    class Meta:
        verbose_name = 'merchant'
        verbose_name_plural = 'merchants'

    def __str__(self):
        return u"{}".format(self.merchant_name)

    