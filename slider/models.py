from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='default_image.png')

    class Meta:
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.name