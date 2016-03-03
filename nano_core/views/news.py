from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def news(request):
    return render_to_response('nano_core/news.html', {
    },
        context_instance=RequestContext(request)
    )
