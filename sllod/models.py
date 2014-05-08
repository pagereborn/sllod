from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

'''
Poll Class
'''
class Poll(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    share = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    '''
    def __init__(self):
        created_by = datetime.datetime.today()
    '''
    def __str__(self):
        
        return self.message
    
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?' 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
            #self.share = 100;
            super(Poll, self).save(*args, **kwargs)
            self.make_option()
        else:
            super(Poll, self).save(*args, **kwargs)
    
    def make_option(self):
        words = self.message.split()
        for word in words:
            if word.find('#') != -1:
                option = Option    
                option.objects.create(poll = self, option_text = word)
'''
Option Class
'''            
class Option(models.Model):
    poll = models.ForeignKey(Poll)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    
    def __str__(self):
        return self.option_text
'''
OptionVote Class
'''       
class OptionVote(models.Model):
    poll = models.ForeignKey(Poll)
    option = models.ForeignKey(Option)
    created_by = models.ForeignKey(User)
    has_changed = models.BooleanField()
    created_at = models.DateTimeField('date created')
    
    class Meta:
        unique_together = ("poll", "option", "created_by")
    
    
