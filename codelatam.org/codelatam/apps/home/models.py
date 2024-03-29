from django.db import models


class userWaiting(models.Model):
    nombre      = models.CharField(max_length=200)
    email       = models.EmailField()
    status      = models.BooleanField(default=True,help_text=" Activo si desea seguir recibiendo informacion")

    def __unicode__(self):
        datos = "%s %s"%(self.nombre,self.email)
        return datos