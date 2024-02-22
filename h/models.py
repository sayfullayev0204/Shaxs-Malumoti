from django.db import models

class Hudud(models.Model):
    Nomi=models.CharField(max_length=500)
    joylashuvi=models.CharField(max_length=700)
    def __str__(self):
        return self.Nomi
class Fuqoro(models.Model):
    hudud=models.ForeignKey(Hudud, on_delete=models.CASCADE) 
    Ismi=models.CharField(max_length=200)
    Familyasi=models.CharField(max_length=200)
    Sharfi=models.CharField(max_length=200) 
    Rasmi=models.ImageField(upload_to='Fuqaro') 
    def __str__(self):
        return self.Ismi
class Jinoyatchi(models.Model):
    hudud=models.ForeignKey(Hudud, on_delete=models.CASCADE)
    Ismi=models.CharField(max_length=200)
    Familyasi=models.CharField(max_length=200)
    Sharfi=models.CharField(max_length=200)    
    Rasmi=models.ImageField(upload_to='jinoyatchi')
    def __str__(self):
        return self.Ismi
class Qarindosh(models.Model):
    bogliq=models.ForeignKey(Fuqoro, on_delete=models.CASCADE)
    Ismi=models.CharField(max_length=200)
    Familyasi=models.CharField(max_length=200)
    Sharfi=models.CharField(max_length=200)    
    Rasmi=models.ImageField(upload_to='qarindosh')
 
    def __str__(self):
        return self.Ismi

class Safarda(models.Model):
    hudud=models.ForeignKey(Hudud, on_delete=models.CASCADE)
    Fuqoro=models.ForeignKey(Fuqoro, on_delete=models.CASCADE)
    Vaqti=models.DateTimeField()
