from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
        if request.POST["action"] == "buy":
            # do nothing for now
            print("buy")
        else:
            try:
                # try to get an existing order
                exist_order = Order.objects.get(owner=request.user, item=item)
                exist_order.item_cnt += cnt
                exist_order.save()
            except Order.DoesNotExist:
                # create a new order
                order = Order(owner=request.user, item=item, item_cnt=cnt)
                order.save()
        return render(request, "taobao/success.html", context)
    else:
        context["item"] = item
        return render(request, "taobao/item_detail.html", context)


@login_required
def shop_cart(request):
    orders = Order.objects.filter(owner=request.user)
    if request.method == 'POST':
        operation = request.POST["operation"]
        # user delete some order
        if operation == "delete":
            oid = request.POST["order_id"]
            orders.get(pk=oid).delete()
        elif operation == "checkout":
            # get all checked orders
            checked_orders = request.POST.getlist("checked_orders")
            print(checked_orders)
            # will only create a new package when at least one order is chosen
            if len(checked_orders) > 0:
                return render(request, "taobao/success.html")
        # api for calculating the total price
        elif operation == "cal_total" and request.is_ajax():
            checked_orders = request.POST.getlist("checked_orders")
            total = 0.0
            for o in checked_orders:
                total += orders.get(pk=o).total()
            return JsonResponse({"total_cart": ("%.2f" % total)})
    total = 0
    for o in orders:
        total += o.total()
    context = {"orders": orders, "total": total}
    return render(request, "taobao/shopping_cart.html", context)


@login_required
def change_cnt(request):
    if request.is_ajax() and request.method == "POST":
        order_id = request.POST["order_id"]
        operation = request.POST["operation"]
        total_cart = float(request.POST["total_cart"])
        order = Order.objects.get(pk=order_id)
        # lower and upper limit --- 1 ~ 99
        if operation == "add" and order.item_cnt < 99:
            order.item_cnt += 1
            order.save()
            total_cart += order.item.price
        elif operation == "minus" and order.item_cnt > 1:
            order.item_cnt -= 1
            order.save()
            total_cart -= order.item.price
        data = {
            # latest count
            "cnt": order.item_cnt,
            # total price for the order
            "total_order": ("%.2f" % order.total()),
            # total price for all
            "total_cart": ("%.2f" % total_cart)
        }
        return JsonResponse(data)
    return JsonResponse({})

