from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('codelatam.apps.home.views',
	url(r'^$','index_view',name="vista_principal"),
)
