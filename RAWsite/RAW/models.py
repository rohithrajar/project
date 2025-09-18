from django.db import models

# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    album=models.CharField(max_length=50)
    file=models.FileField(upload_to='song/')
    audio_link=models.CharField(max_length=50,blank=True,null=True)
    lyrics=models.TextField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by=2
    
    def __str__(self):
        return self.title+" - "+self.artist