from django.db import models
from django.contrib.auth.models import User



# Coleccion de datos

GENDER_CHOICE=(
	('H','Hombre'),
	('M','Mujer'),
)

COUNTRY_CHOICE = (
	('Mexico','Mexico'),
	('Chile','Chile'),
	('Argentina','Argentina'),
	('Peru','Peru'),
)


	
"""
Inician los modelos 
Cada Modelo Representa una tabla en Django
"""

# Tipos de Usuarios
class type(models.Model):
	name = models.CharField(max_length=200,help_text="Nombre del tipo de usuarios")
	description = models.TextField(null=True,blank=True,help_text="Descripcion del tipo")
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.name


# Perfil de Usuario		
class userProfile(models.Model):
	
	def image_path(self,filename):
		url = "MultimediaData/Users/%s/ImageProfile/%s"%(self.user,str(filename))
		return url
	
	user 				= models.ForeignKey(User)
	userType 			= models.ForeignKey(type,help_text="Tipo de usuario")
	aboutMe 			= models.TextField(max_length="500",help_text="Escribe informacion que quieras que conozcan de ti")
	birthDay 			= models.DateField(null=True,blank=True)
	gender 				= models.CharField(max_length=1,choices=GENDER_CHOICE,help_text="Hombre o Mujer")
	country 			= models.CharField(max_length=500,choices=COUNTRY_CHOICE,help_text="Elige tu Pais")
	activationKey   	= models.CharField(max_length=200,null=True,blank=True)
	keyExpires  		= models.DateTimeField(null=True,blank=True)
	image 				= models.ImageField(upload_to=image_path,null=True,blank=True)

	def __unicode__(self):
		return self.user
