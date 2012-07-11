from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('codelatam.apps.home.views',
	url(r'^$','proximamente_view',name="vista_proximamente"),
	url(r'^beta/$','index_view',name="vista_principal"),
	url(r'^beta/about/$','about_view',name="vista_about"),
	url(r'^beta/contacto/$','contact_view',name="vista_contacto"),
)
