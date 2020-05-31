from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rooms.models import *
from django.utils import timezone
import datetime
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'rooms/index.html')

@login_required
def customerslistview(request):
    customers=Customer.objects.all()
    context={
        'customers':customers
    }
    return render(request,'rooms/customer_list.html',context=context)
@login_required
def newCustomerview(request):
    rooms=Room.objects.filter(status=False)
    context={
        'rooms':rooms
    }
    if request.method=="POST":
        try:
            name=request.POST['name']
            email=request.POST['email']
            phonenum=request.POST['contact']
            idproof=request.POST['idProof']
            idnum=request.POST['idProofnum']
            roomnum=request.POST['roomNum']
            room= Room.objects.get(roomid=roomnum)
            room.status=True
            room.save();
            try:
                customer=Customer.objects.create(
                    name=name,
                    phone=phonenum,
                    email=email,
                    room=room,
                    personalid=idproof,
                    idnumber=idnum,
                )
                customer.save()
                return redirect(customerslistview)
            except:
                context={
                'rooms':rooms,
                }
                return render(request,'rooms/new_customer.html',context=context)
            
        except:
            message="Fill all the Fields"
            context={
            'rooms':rooms,
            'msg':message,
            }
            return render(request,'rooms/new_customer.html',context=context)
    return render(request,'rooms/new_customer.html',context=context)

@login_required
def customerDetailview(request,cid):
    customer=Customer.objects.get(pk=cid)
    context={
        'customer':customer,
    }
    if request.method == "POST":
        bill=request.POST['bill']
        customer.bill=bill
        customer.checkout=datetime.datetime.now()
        room=customer.room
        room.status=False
        room.save()
        customer.save()
    return render(request,'rooms/customer_detail.html',context=context)

@login_required
def roomView(request):
    rooms=Room.objects.all()
    context={
        'rooms':rooms
    }
    return render(request,'rooms/rooms.html',context=context)
@login_required
def roomCustomerView(request,rid):
    room=Room.objects.get(pk=rid)
    customer=Customer.objects.get(room=room)
    context={
        'customer':customer,
    }
    return render(request,'rooms/customer_detail.html',context=context)
