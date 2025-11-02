from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.

def index(request):

    # response_data = render_to_string('myapp/myapp.html')
    # return HttpResponse(response_data)

    return render(request,"myapp/myapp.html")

