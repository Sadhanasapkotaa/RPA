from django.db import models
from django.forms import ValidationError


def validate_file_extension(value):
    print(type(value))
    print(value)
    print(value.name)
    if not value.name.endswith('.mp4') and not value.name.endswith('.mvk'):
        raise ValidationError(u'only .mp4 or .mvk file')

# Create your models here
class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="", validators=[validate_file_extension])

    def __str__(self):
        return f'{self.name} : {str(self.videofile)}'