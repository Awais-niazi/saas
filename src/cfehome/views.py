from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def landing_page_view(request):
   return render(request, "landing_page.html")


def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name) 
    return about_view(request, *args, **kwargs)

def about_view(request ):
    my_title = 'This is my home page'
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)
    try:
        percentage = (page_qs.count() * 100.0) / qs.count()
    except:
        percentage = 0    
    my_context = {

        'page_title': my_title,
        'queryset': page_qs.count(),
        'total_page_count': qs.count(),
        'percentage':percentage 
    }
    
    html_templates = 'home.html'
    path = request.path
    print('path', path)
    PageVisit.objects.create(path= request.path)
    return render(request, html_templates, my_context)