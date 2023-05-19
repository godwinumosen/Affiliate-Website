from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
options = {
    ('draft','Draft'),
    ('publish','Publish'),
}
class AffiliateModeSite (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title =  models.CharField(max_length = 200)
    content = models.TextField()
    price = models.CharField(max_length=50)
    offer = models.CharField(max_length=50, choices=options, default='draft')
    slug = models.SlugField(max_length=250)
    
    def __str__(self) :
        return self.title