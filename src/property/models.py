from django.db import models
from django.utils.encoding import smart_str
from users.models import User


class Propriety(models.Model):
    street_address = models.CharField(max_length=150)
    address_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=9)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    coutry = models.CharField(max_length=50)
    complement = models.CharField(max_length=200, null=True, blank=True)
    reference_point = models.CharField(max_length=50, null=True, blank=True)
    
    user_perfil = models.ForeignKey(User, on_delete=models.CASCADE)

    #    latitude = models.FloatField(null=True, blank=True)
    #    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return smart_str('%s %s %s %s' % (
           self.street_address,
           self.address_number,
           self.city,
           self.provice_state))