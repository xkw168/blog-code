from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *


# Create your views here.
def home(request):
    items = Item.objects.all().filter(on_sell=True).order_by("id")
    if request.method == "POST":
        search = request.POST["search"]
        items = items.filter(description__icontains=search)
    context = {"items": items}
    return render(request, "taobao/home.html", context)


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {}
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        cnt = int(request.POST["count"])
        print(cnt)
        return render(request, "taobao/success.html", context)
    else:
        context["item"] = item
        return render(request, "taobao/item_detail.html", context)

