from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import  format_lazy
from faicon.fields import FAIconField


class skillGroup(models.Model):
    title = models.CharField(max_length=200,)
    is_active = models.BooleanField(default=False)
    # slug = models.SlugField(max_length=30, verbose_name='slug', null=True, unique=True)
    
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    skill_group = models.ForeignKey(skillGroup, on_delete= models.CASCADE, related_name='skills_of_group')
    title = models.CharField(max_length=200,)
    percent = models.PositiveIntegerField()
    icon = FAIconField()
    update_date = models.DateTimeField( auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    # slug = models.SlugField(max_length=30, verbose_name='slug', null=True, unique=True)
    
    def __str__(self):
        return self.title