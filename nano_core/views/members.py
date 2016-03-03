from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User

def members(request):
    users = User.objects.all()
    return render_to_response('nano_core/members.html', 
        {
            "users": users,
        },
        context_instance=RequestContext(request)
    )
