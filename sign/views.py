from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Proform
from .models import Product, register, AddCart, Checkout,OrderItem
from des import settings


# Create your views here.
def Register(request):
    if request.method=='POST':
        print(request.POST)
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        username = request.POST['username']
        age=request.POST['age']
        contact=request.POST['contact']
        gender=request.POST['gender']
        address=request.POST['address']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']


        if p1 == p2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username taken..')
                return redirect('/Register/')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email taken.. ')
                return redirect('/Register/')
            else:
                user = User.objects.create_user(username=username, password=p1, email=email, first_name=f_name,last_name=l_name)
                user.save()
                newuser=register.objects.create(user=user,age=age,
                                                contact=contact,gender=gender,address=address)
                newuser.save()
                print('user created')
                return redirect('/login/')
        else:
            messages.error(request,'password not matching..')
            return redirect('/login/')
    else:
        return render(request,'Register.html')

def loginuser(request):
    s=Product.objects.all()
    if request.method == 'POST':
        print(True)
        u = request.POST['Username']
        p1 = request.POST['password']

        user = authenticate(username=u, password=p1)

        if user is not None:
            print(True)
            login(request, user)
            return redirect('/product/')
        elif User.objects.filter(username=u).exists():
            messages.info(request,"password incorrect")
            return redirect('/login/')
        else:
            messages.info(request, "username doesn't exists")
            return redirect('/login/')
    else:
        return render(request, 'login.html',{'s':s})

def logout(request):
    auth.logout(request)
    return redirect('/product/')

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def base(request):
    return render(request,'base.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def product(request):
    s=Product.objects.all().order_by('name')
    return render(request,'product.html',{'s':s})

# def pro(request):
#     if request.method=='POST':
#         f=Proform(request.POST)
def pro_details(request, id):
    s = Product.objects.get(id=id)
    return render(request, 'pro_details.html',{'s':s})
def add_cart(request,id):
    current_user=request.user
    user_id=current_user.id
    print(user_id)

    # s=Product.objects.get(id=id)
    # if request.method=='POST':
    #     user=request.POST['user']
    #     product_id=request.POST['pro_id']
    #     qty=request.POST['qty']
    #     total=request.POST['total']
    return render(request,'add_cart.html',{'user_id':user_id})


def product_list(request):
    s = Product.objects.all()
    return render(request, 'product.html', {'s':s})


def view_cart(request):
    s = AddCart.objects.filter(user=request.user)
    for i in s:
        print(i.product_id.price)
    total_price = sum(item.product_id.price * item.qty for item in s)
    return render(request, 'add_cart.html', {'s': s,'total_price':total_price})


def add_to_cart(request,pid):
    u=request.user.id
    uid = request.user.id
    # cartnum = AddCart.objects.filter(user=uid).count()
    # favnum=Product.objects.filter(user=uid).count()
    pro=Product.objects.get(id=pid)

    print(u,'uiddddddddddd')
    if request.method == 'POST':
        pid=request.POST['product_id']
        qty=int(request.POST['qty'])
        price=int(request.POST['price'])
        print(pid,'ppppppppiiiiid')
        print(qty)
        print(price)
        # return HttpResponse('dataaaa')


        # cart = AddCart(user_id=u, product_id_id=pid, qty=1, total=1 * pro.price)
        # cart.save()-
        # return redirect('/cart/')

        if AddCart.objects.filter(user=u,product_id=pid):
            data=AddCart.objects.get(product_id=pid,user=u)
            data.qty=data.qty+qty
            print(data.qty,'qtyyyyy')
            data.total=data.qty*price
            print(data.total)
            # data.total=data.total+total_price
            # print(total_price)
            data.save()
            cart=AddCart.objects.filter(user=u,product_id_id=pid).update(qty=qty,total=qty*price)
            return redirect('/cart/')
        # else:
        #     cart = AddCart(user_id=u,product_id_id=pid,qty=qty,total=qty*price)
        #     cart.save()
        # return HttpResponse('product added in your cart')
        # return redirect('/cart/')
        print(pid)
    elif AddCart.objects.filter(user=u,product_id=pid):
        data = AddCart.objects.get(product_id=pid, user=u)
        data.qty = data.qty + 1
        print(data.qty, 'qtyyyyy')
        data.total = data.qty * pro.prize
        print(data.total)
        # data.total=data.total+total
        # print(total)
        data.save()
        # cart=AddCart.objects.filter(user=u,product_id=pid).update(qty=qty,total=qty*price)
        return redirect('/cart/')


    else:
        cart = AddCart(user_id=u, product_id_id=pid, qty=1, total=1 * pro.price)
        cart.save()
        return redirect('/cart/')
    return render(request,'pro_details.html',{'pro':pro})


def remove_from_cart(request, id):
    s = AddCart.objects.get(id=id)
    s.delete()
    return redirect('/cart/')

# def checkout(request):
#     u=request.user.id
#     s=CheckOut.objects.all()
#     if request.method=='POST':
#
#         f_name=request.POST['firstname']
#         l_name=request.POST['lastname']
#         username=request.POST['username']
#         email=request.POST['email']
#         address=request.POST['address']
#         address2=request.POST['address2']
#         country=request.POST['country']
#         state=request.POST['state']
#         zip=request.POST['zip']
#
#         check=CheckOut(user=u,product_id_id=id,f_name=f_name,l_name=l_name,username=username,email=email,
#                        address=address,address2=address2,country=country,
#                        state=state,zip=zip)
#         check.save()
#         return HttpResponse('checkout thai gayu namuna')
#     return render(request,'checkout.html',{'s':s})

def checkout(request):
    if request.method=="POST":
        user = request.user.id
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        zip = request.POST['zip']

        print(user,f_name,l_name,username,email,address,country,state,zip)

        cart=AddCart.objects.filter(user=user)
        for i in cart:
            print(i.product_id.name,'sdfghjkhjk')
        check=Checkout(user_id=user,f_name=f_name,l_name=l_name,username=username,
                      email=email,address=address,country=country,state=state,zip=zip)
        check.save()
        # total=sum(i.total for i in cart)
        # print(total,'tooooooooooooooooo')
        # print(cart)
        return render(request,'checkout.html',{'cart': cart})
    else:
        print('dinchak')
        user = request.user.id
        cart = AddCart.objects.filter(user=user)
        for i in cart:
            print(i.product_id.name, 'sdfghjkhjk')
        return render(request,'checkout.html',{'cart':cart})
        # return HttpResponse('ok ')
        # order_details = "\n".join([
        #     f"Product: {c.pro.name}, Quantity: {c.quantity}, Price: {c.pro.price}, Total Price: {c.total}"
        #     for c in cart
        # ])
        o=OrderItem(user_id=user, name=name,email=email,address=address,phone=phone,info=info,total_price=total_price)
        o.save()
        for c in cart:
            cart_item=OrderItem(
                user_id=user,
                order_id=o.id,
                prod_id=c.pro,
                image=c.pro.image,
                quantity=c.quantity,
                price=c.pro.price,
                total_price=c.total


            )
            cart_item.save()
            cart.delete()
            print('cart_item')
        print(o,'ooooorderrrrrrrrrrrrrrrrrrrrrrr')
        subject = 'Order Confirmation'
        message = f"Dear {name},\n\nYour order has been successfully placed!\n\nOrder Details:\n{order_details}\n\nTotal Price: {total}\n\nThank you for shopping with us!"
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]  # Change this if you want to send to a different email address

        send_mail(subject, message, from_email, to_email)

        messages.success(request, 'Order successfully placed! Thanks for shopping, visit again.')
        return HttpResponse('dinchak')
        # return HttpResponse("Data is printed in terminal")
