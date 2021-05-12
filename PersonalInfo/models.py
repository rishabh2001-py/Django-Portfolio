from django.db import models


class Jobs(models.Model):
    image=models.ImageField( upload_to="images/", height_field=None, width_field=None, max_length=None)

    summary=models.CharField(max_length=200)

    def __str__(self):
        return self.summary
    

