from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os

# Create your models here.

#~ Function that create a p_img path for every users
def profile_img_directory(instance,filename):
    extension = filename.split('.')[-1] # get the img extension ~jpg, png etc
    foldername = f'{instance.user.id}'
    filename = f'{instance.user.username}.{extension}'
    return f'profile_img/{foldername}/{filename}'

#+ CustonUser Table
class CustomUser(models.Model):
    user = models.OneToOneField(User, verbose_name=("User_table"), on_delete=models.CASCADE)
    #~ extra fields
    birth_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    city = models.CharField('Sehir', null=True, blank=True, max_length=30)
    profile_img = models.ImageField('profil_resmi', upload_to=profile_img_directory, height_field=None, width_field=None, max_length=None, default='profile_img/default/avatar.png')
    
    def calculate_age (self):
        if self.birth_date:
            today = datetime.today()
            user_age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return user_age
        else:
            return None

    def save(self):
        if self.pk:
            try:
                old_file = CustomUser.objects.get(pk=self.pk)
                if old_file.profile_img and self.profile_img != old_file.profile_img:
                    # delete old profile img
                    os.remove(old_file.profile_img.path)
            except CustomUser.DoesNotExist:
                pass
        super().save()

    def __str__(self):
        return self.user.username