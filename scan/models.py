from django.db import models
from django.contrib.auth.models import User

class ScanData(models.Model):
    '''Scan model, to keep track of scan records'''

    id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barcode_number = models.CharField(max_length=20, null=True,blank=True)
    scanned_at = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.id
    


