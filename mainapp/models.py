from django.db import models


# Create your models here.

class SocialMediaLinks(models.Model):
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    skype = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

class PersonalInformation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, null=True, blank=True)
    availiability = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(max_length=200, null=True, blank=True)
    birhtday = models.DateField()
    age = models.IntegerField()
    aboutme = models.TextField()

class Website(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    logo = models.ImageField(max_length=255)
    bg = models.ImageField(max_length=255)
    profile = models.ImageField(max_length=255)

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    review = models.TextField()
    profile = models.ImageField(max_length=255)

class Skill(models.Model):
    html = models.IntegerField()
    css = models.IntegerField()
    javascript = models.IntegerField()
    php = models.IntegerField()
    wordpress = models.IntegerField()
    android = models.IntegerField()

class Fact(models.Model):
    clients = models.IntegerField()
    projects = models.IntegerField()
    supporthour = models.IntegerField()
    worker = models.IntegerField()

class Resume(models.Model):
    cv = models.FileField()

class Category(models.Model):
    title = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    image = models.ImageField(max_length=255)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=255)


