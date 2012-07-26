from django.shortcuts import render_to_response
from django.template import RequestContext
from codelatam.apps.home.forms import sendInformationFORM
from codelatam import settings
from django.core.mail import EmailMultiAlternatives
from codelatam.apps.home.models import userWaiting

def proximamente_view(request):
    if request.POST:
        form = sendInformationFORM(request.POST) # Creamos un formulario con la informacion enviada de POST
        if form.is_valid(): # Si la informacion es valida entonces
            # Guardamos el usuario que quiere mantenerse informado
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            u = userWaiting() # Creamos una nueva instancia
            u.nombre = nombre
            u.email = email
            u.status = True
            u.save() # Guardamos la informacion del usuario
            # Enviamos el correo
            subject = 'Hola Coder!'
            from_email = 'hola@codelatam.org'
            to = email
            text_content = ''
            html_content = 'Gracias %s por tu interes por formar parte de esta nueva comunidad hispana para programadores </br> Te mantendremos informado de nuestra fecha de Lanzamiento'%(nombre)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    form = sendInformationFORM() # Creamos un nuevo form
    ctx = {'form':form}
    return render_to_response('proximamente.html',ctx,context_instance=RequestContext(request))

def index_view(request):
	return render_to_response('home/index1.html',context_instance=RequestContext(request))

