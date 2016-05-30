from django.db import models


class ImageUser(models.Model):
    id_image = models.CharField(max_length=80)
    image = models.ImageField(
            upload_to="static/img/",
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
