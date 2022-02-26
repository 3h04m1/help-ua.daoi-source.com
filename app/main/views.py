from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Help, NeedHelp

def index(request):
    # help = Help.objects.order_by("pub_date")()
    # context = {
    #     "help": help,
    # }
    return render(request, "main/index.html")


def help(request):
    if request.method == "POST":
        print(request.POST)
        help = Help.objects.create(help_type=request.POST.get("help_type"),
            name = request.POST.get("name"),
            tel = request.POST.get("tel"),
            details=request.POST.get("details"),
            link=request.POST.get("link"),
            address=request.POST.get("address")
        )
        return redirect('index')

    help = Help.objects.order_by("pub_date")
    context = {
        "help": help,
    }
    return render(request, "main/help.html", context=context)

def need_help(request):
    if request.method == "POST":
        help = NeedHelp.objects.create(
                help_type=request.POST.get("help_type"),
                name = request.POST.get("name"),
                tel = request.POST.get("tel"),
                details=request.POST.get("details"),
                link=request.POST.get("link")
            )
    help = NeedHelp.objects.order_by("pub_date")
    context = {
        "help": help,
    }
    return render(request, "main/need_help.html", context=context)




def mapview(request):
    help = Help.objects.order_by("pub_date")
    context = {
        "help": help,
    }

    return render(request, "working.html")

def betamap(request):
    help = Help.objects.order_by("pub_date")
    context = {
        "help": help,
    }

    return render(request, "map.html")

def help_list(request):
    help_list = Help.objects.order_by("pub_date")
    paginator = Paginator(help_list, 21)
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

    }
    return render(request, "main/help_list.html", context=context)

def need_help_list(request):
    help_list = NeedHelp.objects.order_by("pub_date")
    paginator = Paginator(help_list, 21)
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

    }
    return render(request, "main/help_list.html", context=context)
# Create your views here.
