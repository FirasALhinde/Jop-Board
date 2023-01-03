from django.db import models
from django.utils.text import slugify
# Create your models here.
JOP_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename,extention = filename.split('.')
    # return 'jops/%s/%s.%s'%(instance.id,instance.id,extention)
    return 'jops/%s.%s'%(instance.id,extention)  

class Jop(models.Model):
    title = models.CharField(max_length=100)
    # location 
    jop_type = models.CharField(max_length=50,choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True,null=True )
    
    def save(self,*args,**kwargs):
        #logic
        self.slug=slugify(self.title) 
        super(Jop,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name


class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    jop = models.ForeignKey(Jop,related_name='apply_jop',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name