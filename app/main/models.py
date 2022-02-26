# from pyexpat import model
from django.db import models

class Help(models.Model):
    help_type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    pub_date = models.TimeField(auto_now_add=True)
    mod_date = models.TimeField(auto_now=True)
    link = models.URLField(max_length=1000, blank=True)
    
    class Adress(models.TextChoices):
        chisinau = "chisinau", "chisinau"
        balti = "balti", "balti"
        comrat = "comrat", "comrat"
        anenii_noi = "anenii_noi", "anenii_noi"
        basarabeasca = "basarabeasca", "basarabeasca"
        briceni = "briceni", "briceni"
        cahul = "cahul", "cahul"
        cantemir = "cantemir", "cantemir"
        calarasi = "calarasi", "calarasi"
        causeni = "causeni", "causeni"
        cimislia = "cimislia", "cimislia"
        criuleni = "criuleni", "criuleni"
        donduseni = "donduseni", "donduseni"
        drochia = "drochia", "drochia"
        dubasari = "dubasari", "dubasari"
        edinet = "edinet", "edinet"
        falesti = "falesti", "falesti"
        floresti = "floresti", "floresti"
        glodeni = "glodeni", "glodeni"
        hincesti = "hincesti", "hincesti"
        ialoveni = "ialoveni", "ialoveni"
        leova = "leova", "leova"
        nisporeni = "nisporeni", "nisporeni"
        ocnita = "ocnita", "ocnita"
        orhei = "orhei", "orhei"
        rezina = "rezina", "rezina"
        riscani = "riscani", "riscani"
        singerei = "singerei", "singerei"
        soroca = "soroca", "soroca"
        straseni = "straseni", "straseni"
        soldanesti = "soldanesti", "soldanesti"
        stefan_voda = "stefan_voda", "stefan_voda"
        taraclia = "taraclia", "taraclia"
        telenesti = "telenesti", "telenesti"
        ungheni = "ungheni", "ungheni"
    
    address = models.CharField(max_length=1000, choices=Adress.choices, default="chisinau")
    valabil = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.help_type} - {self.address}"
    

class NeedHelp(models.Model):
    help_type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    pub_date = models.TimeField(auto_now_add=True)
    mod_date = models.TimeField(auto_now=True)
    link = models.URLField(max_length=1000, blank=True)
    # address = models.CharField(max_length=1000, default="Moldova")
    valabil = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.help_type} - {self.pub_date}"
# Create your models here.
