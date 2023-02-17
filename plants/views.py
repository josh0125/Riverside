from django.shortcuts import render
from .models import Plant, Category

# Create your views here.


# INDEX PAGE
def indexPage(request):
    data = Plant.objects.all()

    context = {
        "plant" : data 
    }
    return render(request, 'plants/index.html', context)

# ABOUT PAGE
def aboutPage(request):
    data = Plant.objects.all()

    context = {
        "plant" : data 
    }
    return render(request, 'plants/about.html', context)


# PLANT PAGE
def plantPage(request):
    data = Plant.objects.all()

    context = {
        "plants" : data
    }
    return render(request, 'plants/plants.html', context)

def onePlantDisplayPage(request, iID):
    data = Plant.objects.get(id=iID)
    print(data.botanical_name)
    context = {
        "plant" : data 
    }
    return render(request, 'plants/display.html', context)


# CATEGORY PAGES
def categoryPage(request):
    data = Category.objects.all()

    context = {
        "categories" : data
    }
    return render(request, 'plants/category.html', context)

# Filters all Plants with that specific category
def categoryDisplayPage(request, sName):
    category = Category.objects.get(name=sName)


    data = Plant.objects.filter(category = category)

    context = {
        "plants" : data 
    }
    return render(request, 'plants/plants.html', context)

