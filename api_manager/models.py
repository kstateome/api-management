from django.db import models


class KeyManager(models.Manager):
    def active(self):
        return Keys.objects.filter(active=True)

class Keys(models.Model):
    key = models.CharField(max_length=250)
    key_user = models.CharField(max_length=250)
    active = models.BooleanField()
    
    objects = KeyManager()
    
    def __unicode__(self):
        return self.key
    
class KeyUsage(models.Model):
    key = models.ForeignKey(Keys)
    log_message = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.log_message
    