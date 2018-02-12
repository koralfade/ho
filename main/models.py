from django.db import models

class Bron(models.Model):
    email = models.EmailField(default='mail@mail.ru')
    name = models.CharField(max_length=128, default='ruslan')
    phone_number = models.IntegerField(max_length=12, default='89097552700')
    
