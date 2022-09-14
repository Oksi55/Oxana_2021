from django.db import models

# Create your models here.
class Project(models.Model):
    author = models.CharField(max_length=80)
    body = models.TextField('Содержание', blank=True)
    cteated_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('this_post', on_delete=models.CASCADE)

class this_post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


