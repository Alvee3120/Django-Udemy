from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challanges_dictionary = {
        "january": "Plan your goals for the new year and start learning a new skill.",
        "february": "Celebrate a holiday, like Lunar New Year or Valentine's Day, and catch up on indoor reading.",
        "march": "Do some early spring cleaning and declutter your living space.",
        "april": "Spend time outdoors, start your gardening project, or visit a local park.",
        "may": "Prepare for summer travel by booking your vacation or weekend trips.",
        "june": "Enjoy the beginning of summer by attending a local outdoor festival or concert.",
        "july": "Host a BBQ or picnic with friends and try out a new grilling recipe.",
        "august": "Visit a beach, lake, or pool to beat the heat, and finish your summer reading list.",
        "september": "Start a new fitness routine and embrace the cozy autumn transition.",
        "october": "Visit a pumpkin patch, carve a jack-o'-lantern, or watch a spooky movie marathon.",
        "november": "Reflect on what you're grateful for and volunteer for a charitable cause.",
        "december": "Decorate for the holidays and spend quality time with family and friends."
}



def monthly_challanges_by_number(reques,month):
    months = list(monthly_challanges_dictionary.keys())

    if month > len(months):
        return HttpResponseNotFound("Not Supported month")

    redirect_month = months[month-1]
    return HttpResponseRedirect("/challanges/" + redirect_month)

def monthly_challanges(request,month):
   
    try:
       text = monthly_challanges_dictionary[month]
       return HttpResponse(text)
    
    except:
        return HttpResponseNotFound("not valid")

    