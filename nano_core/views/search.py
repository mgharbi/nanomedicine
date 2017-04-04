import re

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q

from ..models import UserProfile
from django.contrib.auth.models import User

def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    search_query = ""
    user_results = None

    if "search_query" in request.GET and request.GET['search_query'].strip():
        search_query = request.GET["search_query"]
        q = get_query(search_query, ["first_name", "last_name" ])
        user_results = User.objects.filter(q)

    return render_to_response('nano_core/search.html', 
    {
        "search_query": search_query,
        "user_results": user_results
    },
        context_instance=RequestContext(request)
    )
