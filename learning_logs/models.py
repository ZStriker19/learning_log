from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    '''A topic the user is learning about'''
    tex = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        '''return a string representation of the model'''
        return self.tex
    
class Entry(models.Model):
    '''Something specific learned about a topic'''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        '''Return a string representation of the model.'''
        if len(self.text) > 50:
            return self.text + "..."
        else:
            return self.text