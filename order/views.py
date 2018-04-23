from django.shortcuts import render,get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

def thanks(request,order_id):
    if order_id:
        customer_order = get_object_or_404(Order,id=order_id)
    return render(request,'thanks.html',{'customer_order':customer_order})

@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        print("hi")
        order_details = Order.objects.filter(emailAddress=email)
        print(order_details)
    return render(request,'order/orders_list.html',{'order_details':order_details})
# Create your views here.
@login_required
def viewOrder(request,order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id,emailAddress=email)
        order_items = OrderItem.objects.filter(order=order)
    return render(request,'order/order_detail.html',{'order':order,'order_items':order_items})
