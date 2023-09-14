from django.db import models
from django.contrib.auth.models import User

class BarcodeData(models.Model):
    '''Scan model, to keep track of scan records'''

    id = models.CharField(max_length=1000, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barcode_number = models.CharField(max_length=100)
    scanned_at = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.id
    


