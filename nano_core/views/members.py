from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def members(request, member_id = None):
    if member_id is not None:
        all_users = User.objects.filter(id=member_id)
    else:
        all_users = User.objects.all()

    paginator =  Paginator(all_users,10)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_pages)
    return render_to_response('nano_core/members.html', 
        {
            "users": users,
        },
        context_instance=RequestContext(request)
    )
