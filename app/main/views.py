from unicodedata import category
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Help, NeedHelp
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")

def index(request):
    # help = Help.objects.order_by("mod_date")()
    # context = {
    #     "help": help,
    # }
    return render(request, "main/index.html")


def help(request):
    if request.method == "POST":
        # print(request.POST)
        help = Help.objects.create(
            title=request.POST.get("help_type"),
            name = request.POST.get("name"),
            tel = request.POST.get("tel"),
            details=request.POST.get("details"),
            link=request.POST.get("link"),
            address=request.POST.get("address"),
            category=request.POST.get('category')

        )
        return redirect('index')

    help = Help.objects.order_by("mod_date")
    context = {
        "help": help,
    }
    return render(request, "main/help.html", context=context)

def need_help(request):
    if request.method == "POST":
        help = NeedHelp.objects.create(
                title=request.POST.get("help_type"),
                name = request.POST.get("name"),
                tel = request.POST.get("tel"),
                details=request.POST.get("details"),
                link=request.POST.get("link"),
                category=request.POST.get('category')
            )
    help = NeedHelp.objects.order_by("mod_date")
    context = {
        "help": help,
    }
    return render(request, "main/need_help.html", context=context)




def mapview(request):
    help = Help.objects.order_by("mod_date")
    address = request.GET.get("address")
    if address:
        help = help.filter(address=address)
   
    paginator = Paginator(help, 6)

    page_number = request.GET.get('page', 1)

    try:
        help = paginator.page(page_number)
    except PageNotAnInteger:
        help = paginator.page(1)
    except EmptyPage:
        page_number = paginator.page(paginator.num_pages)
    
    page_obj = paginator.get_page(page_number)

    
    context = {
        "help": help,
        "page_obj": page_obj,
        "page_number": page_number,
        "address": address,
    }

    return render(request, "working.html", context=context)

def betamap(request):
    help = Help.objects.all()
    coordonates = {}
    for item in help:
        if item.address:
            # print(item.address)
            location = geolocator.geocode(item.address)
            if location:
                coordonates[item.pk] = [location.latitude, location.longitude]
    context = {
        "help": help,
        "coords": coordonates,
    }
    # print(help)

    return render(request, "map.html", context=context)

def help_list(request):
    help_list = Help.objects.order_by("-pk")
    all_list = help_list
    
    help_type = request.GET.get("category")
    
    address = request.GET.get("address")
    
    
    if address:
        help_list = help_list.filter(address=address)
    if help_type:
        help_list = help_list.filter(category=help_type)


    if help_list:
        paginator = Paginator(help_list, 21)
    else:
        paginator = Paginator(all_list, 21)
    
    page_number = request.GET.get('page', 1)
    
    try:
        help = paginator.page(page_number)
    except PageNotAnInteger:
        help = paginator.page(1)
    except EmptyPage:
        page_number = paginator.page(paginator.num_pages)
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        "help": help,
        "page_obj": page_obj,
        "page_number": page_number,
        "help_list": help_list,
        "help_type": help_type,
        "address": address,

    }
    return render(request, "main/help_list.html", context=context)

def need_help_list(request):
    
    help_type = request.GET.get("help_type")
    
    help_list = NeedHelp.objects.order_by("-pk")
    all_list = help_list
    
    address = request.GET.get("address")

    if help_list:
        paginator = Paginator(help_list, 21)
    else:
        paginator = Paginator(all_list, 21)

    page_number = request.GET.get('page', 1)
    try:
        help = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
    except EmptyPage:
        page_number = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    context = {
        "help": help,
        "page_obj": page_obj,
        "page_number": page_number,
        "help_list": help_list,
        "help_type": help_type,
        "address": address,

    }
    return render(request, "main/help_list.html", context=context)
# Create your views here.
