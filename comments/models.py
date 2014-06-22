from django.db import models
from sllod.models import Poll, Option
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    poll_id = models.ForeignKey(Poll)
    friend_id = models.ForeignKey(User)
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
            #self.share = 100;
            super(Comment, self).save(*args, **kwargs)
            self.make_option()
        else:
            super(Comment, self).save(*args, **kwargs)
    
    def make_option(self):
        words = self.message.split()
        for word in words:
            if word.find('#') != -1:
                option = Option    
                option.objects.create(poll = self, option_text = word)