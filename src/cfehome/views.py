from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    my_title = 'This is my home page'
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)
    my_context = {

        'page_title': my_title,
        'queryset': page_qs.count(),
        'total_page_count': qs.count(),
        'percentage':(page_qs.count() * 100.0) / qs.count(), 
    }
    
    html_templates = 'home.html'
    path = request.path
    print('path', path)
    PageVisit.objects.create(path= request.path)
    return render(request, html_templates, my_context)