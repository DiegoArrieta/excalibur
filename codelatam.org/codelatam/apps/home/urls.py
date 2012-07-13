from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('codelatam.apps.home.views',
	url(r'^beta/$','index_view',name="vista_principal"),
	url(r'^$','proximamente_view',name="vista_proximamente"),
)
