from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.


monthly_challanges_dictionary = {
        "january": "Plan your goals for the new year and start learning a new skill.",
        "february": "Celebrate a holiday, like Lunar New Year or Valentine's Day, and catch up on indoor reading.",
        "march": "Do some early spring cleaning and declutter your living space.",
        "april": "Spend time outdoors, start your gardening project, or visit a local park.",
        "may": None,
        "june": "Enjoy the beginning of summer by attending a local outdoor festival or concert.",
        "july": "Host a BBQ or picnic with friends and try out a new grilling recipe.",
        "august": None,
        "september": "Start a new fitness routine and embrace the cozy autumn transition.",
        "october": "Visit a pumpkin patch, carve a jack-o'-lantern, or watch a spooky movie marathon.",
        "november": "Reflect on what you're grateful for and volunteer for a charitable cause.",
        "december": None
}



def monthly_challenges(request,month):

    # response_data = render_to_string('myapp/myapp.html')
    # return HttpResponse(response_data)
    
    monthly_advice = monthly_challanges_dictionary[month]

    return render(request,"myapp/myapp.html",{
        "month_name" : month.capitalize(),
        "advice" : monthly_advice
    })

def index(request):

    months = list(monthly_challanges_dictionary.keys())

    return render(request , "myapp/index.html", {

        "months" : months

    })