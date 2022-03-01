# from pyexpat import model
from django.db import models

class Help(models.Model):
    title = models.CharField(max_length=20, db_column="title")
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    # pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
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
    
    class Category(models.TextChoices):
        cazare = "cazare", 'Cazare | Проживання'
        transport = "transport", 'Transport | Транспорт'
        consiliere = "consiliere", 'Consiliere | Консультування'
        voluntariat = 'voluntariat', 'Волонтерство, переклад'
        donatii = 'donatii', 'Haine, alimente | Одяг, їжа'
        lucru = 'lucru', 'Lucru | Работа '
    
    category = models.CharField(max_length=20, choices=Category.choices, null=True, default="None")
    
    def __str__(self):
        return f"{self.title}"
    

class NeedHelp(models.Model):
    title = models.CharField(max_length=20,db_column="title")
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    # pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=1000, blank=True)
    valabil = models.BooleanField(default=True)
    
    class Category(models.TextChoices):
        cazare = "cazare", 'Cazare | Проживання'
        transport = "transport", 'Transport | Транспорт'
        consiliere = "consiliere", 'Consiliere | Консультування'
        voluntariat = 'voluntariat', 'Волонтерство, переклад'
        donatii = 'donatii', 'Haine, alimente | Одяг, їжа'
        lucru = 'lucru', 'Lucru | Работа '
    
    category = models.CharField(max_length=20, choices=Category.choices, null=True, default="None")
    
    def __str__(self):
        return f"{self.category}"
# Create your models here.
