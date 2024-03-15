from django.db import models

# Create your models here.


class Certificate(models.Model):
    certificate_id = models.IntegerField()
    certificate_file = models.FileField(upload_to="certificates/")

    def __str__(self):
        return f"Certificate ID: {str(self.certificate_id)}"