from django.shortcuts import render_to_response
from django.template import RequestContext


def proximamente_view(request):
	return render_to_response('proximamente.html',context_instance=RequestContext(request))

def index_view(request):
	return render_to_response('home/index1.html',context_instance=RequestContext(request))

