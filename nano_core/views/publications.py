from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def publications(request):
    return render_to_response('nano_core/publications.html', {
    },
        context_instance=RequestContext(request)
    )
