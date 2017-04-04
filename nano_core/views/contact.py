from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def contact(request):
    return render_to_response('nano_core/contact.html', {
    },
        context_instance=RequestContext(request)
    )
