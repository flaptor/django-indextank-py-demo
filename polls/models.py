from django.db import models
from django.conf import settings
from indextank_client import ApiClient

import datetime

_api = ApiClient(settings.API_URL)
_index = _api.get_index(settings.INDEX_NAME)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    
    def save(self):
        super(Poll, self).save()
        _index.add_document(self.id, {'text': self.question})

    def delete(self):
        _index.delete_document(self.id)
        super(Poll, self).delete()
    
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.choice
    

