from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('codelatam.apps.home.views',
	url(r'^$','index_view',name="vista_principal"),
	url(r'^about/$','about_view',name="vista_about"),
	url(r'^contacto/$','contact_view',name="vista_contacto"),
)
