from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext as _

def home(request):
    return render_to_response('nano_core/home.html', {
    },
        context_instance=RequestContext(request)
    )

def home_files(request,filename):
   return render(request, filename, {}, content_type="text/plain")
