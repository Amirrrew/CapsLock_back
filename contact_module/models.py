from django.db import models

class ContactMessage(models.Model):
    phone = models.CharField(max_length=11 ,verbose_name='Phone number')
    email = models.CharField(max_length=200,null=True ,blank=True ,verbose_name='Email address')
    text = models.TextField(max_length=10000 ,null=True ,blank=True ,verbose_name='Content')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'Contact Messages'