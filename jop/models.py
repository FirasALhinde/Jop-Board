from django.db import models
from django.utils import timezone
# Create your models here.
JOP_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Jop(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published = models.DateTimeField(default=timezone.now)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    # category =
    experience = models.IntegerField(default=1)
    def __str__(self):
        return self.title