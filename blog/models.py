from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        # kind of like moment in js, strftime allows you to pass in arguments to fully customize your time display
        return self.pub_date.strftime('%b %e %Y')
