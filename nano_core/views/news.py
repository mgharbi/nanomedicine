from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ..models import News

def news(request):
    news = News.objects.all()
    return render_to_response('nano_core/news.html', {
        "news": news,
    },
        context_instance=RequestContext(request)
    )
