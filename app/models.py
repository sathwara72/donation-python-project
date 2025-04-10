from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.ImageField(upload_to='donor',null=True, blank=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.ImageField(upload_to='volunteer',null=True, blank=True)
    idpic = models.ImageField(upload_to='volunteer',null=True, blank=True)
    aboutme = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=20,null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300, null=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username
    
class DonationArea(models.Model):
    areaname = models.CharField(max_length=100)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname
    
DONATION_CHOICES=(
         ('Food Donation','Food Donation'),
        ('Cloth Donation','Cloth Donation'),
        ('Blood Donation','Blood Donation'),
        ('Books Donation','Books Donation'),
        ('Furniture Donation','Furniture Donation'),
        ('Vessel Donation','Vessel Donation'),
        ('Organ Donation','Organ Donation'),
        ('Art Donation','Art Donation'),
        ('Cash Donation','Cash Donation'),
        ('Medical Donation','Medical Donation'),
        ('Plant Donation','Plant Donation'),
        ('Other Donation', 'Other Donation'),

    )
    
class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(choices=DONATION_CHOICES,max_length=100,null=True)
    donationpic = models.ImageField(upload_to='donation',null=True, blank=True)
    collectionloc = models.CharField(max_length=300,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)
    donationdate = models.DateField(null=True)
    adminremark = models.CharField(max_length=200, null=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE,null=True)
    donationarea = models.ForeignKey(DonationArea, on_delete=models.CASCADE,null=True)
    volunteermark = models.CharField(max_length=200, null=True)
    updationdate = models.DateField(null=True)
    def __str__(self):
        return str(self.id)

class Gallery(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    deliverypic = models.ImageField(upload_to='gallery',null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)  
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
        



        
