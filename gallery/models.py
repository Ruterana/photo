from django.db import models

# Create your models here.
class Location(models.Model):
    location_name= models.CharField(max_length =30,unique=True)
    def __str__(self):
        return self.location_name
    def save_location(self):
        self.save()
class Category(models.Model):
    category_name = models.CharField(max_length =30,unique=True) 
    def __str__(self):
        return self.category_name
    def save_category(self):
        self.save()
   
class Image(models.Model):
    image_name= models.CharField(max_length=30)  
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category,db_column="category_name")
    image_path = models.ImageField(upload_to = 'pictures/')
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def image(cls):
        image = cls.objects.all()
        return image
    @classmethod
    def search_by_category_name(cls,search_term):
        category= cls.objects.filter(category__category_name__contains=search_term)
        return category
    
    @classmethod
    def filter_by_location(cls, id):
      image= Image.objects.filter(location_id=id)
      return image