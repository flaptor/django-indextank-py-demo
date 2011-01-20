from django.db import models
from datetime import datetime

class Entry(models.Model):
    submit_date = models.DateTimeField(default=datetime.now(), blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField(max_length=5000)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return _("%(name)s on %(date)s") % {'name' : self.name, 
                                            'date' : self.submit_date}

