from django.shortcuts import render, redirect
from .models import Plant, Category

# Create your views here.


# INDEX PAGE
def indexPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/index.html', context)

# ABOUT PAGE
def aboutPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/about.html', context)


# PLANT PAGE
def plantPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plants" : data,
        "categories" : categories
    }
    return render(request, 'plants/plants.html', context)

def onePlantDisplayPage(request, iID):
    data = Plant.objects.get(id=iID)
    categories = Category.objects.all()
    #print(data.botanical_name)

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/display.html', context)


# CATEGORY PAGES
def categoryPage(request):
    data = Category.objects.all()
    categories = Category.objects.all()

    context = {
        "categories" : data
    }
    return render(request, 'plants/category.html', context)

# Filters all Plants with that specific category
def categoryDisplayPage(request, sName):
    category = Category.objects.get(name=sName)
    categories = Category.objects.all()


    data = Plant.objects.filter(category = category)

    context = {
        "plants" : data,
        "category" : category,
        "categories" : categories
    }
    return render(request, 'plants/plants.html', context)


# Search Pages
def searchPage(request):
    search = (request.GET['search'])
    data = Plant.objects.filter(variety__icontains=search)

    categories = Category.objects.all()
    context = {
        "plants" : data,
        "categories" : categories,
        "search": search
    }

    return render(request, 'plants/plants.html', context)
