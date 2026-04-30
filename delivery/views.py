from django.shortcuts import render
from django.http import HttpResponse
from .models import user,Restaurant,Item,Cart,Order,OrderItem
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import razorpay
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def say_hello(request):
    return render(request,"index.html")

def open_signup(request):
    return render(request,"signup.html")

def open_signin(request):
    return render(request,"signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        
        if user.objects.filter(email=email).exists():
           return HttpResponse("This email is already ragisterd Please use a different email.")
        users = user(username=username,password=password,email=email,mobile=mobile,address=address)
        users.save()
        return render(request,"signin.html")
    
    else:
        return HttpResponse("Invaild Response")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


    try:
        user.objects.get(username = username, password = password)
        if username == 'admin':
            return render(request, 'admin_home.html')
        else:
            restaurantList = Restaurant.objects.all()
            return render(request, 'customer_home.html',{"restaurantList" : restaurantList, "username" : username})

    except user.DoesNotExist:
        return render(request, 'fail.html')


def open_add_restaurant(request):
   return render(request,'add_restaurant.html')


def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        
        try:
            Restaurant.objects.get(name = name)
            return HttpResponse("Duplicate restaurant!")
            
        except:
            Restaurant.objects.create(
                name = name,
                picture = picture,
                cuisine = cuisine,
                rating = rating,
            )
        #return HttpResponse("Successfully Added !")
        return render(request, 'admin_home.html')

def show_restaurant(request):
    restaurantList = Restaurant.objects.all()
    return render(request,'show_restaurant.html', {"restaurantList":restaurantList})

def open_update_restaurant(request,restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    return render(request, 'update_restaurant.html', {"restaurant" : restaurant})

def update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        restaurant.name = name
        restaurant.picture = picture
        restaurant.cuisine = cuisine
        restaurant.rating = rating

        restaurant.save()
    restaurantList = Restaurant.objects.all()
    return render(request, 'show_restaurant.html', {"restaurantList" : restaurantList})

def delete_restaurant(request,restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    restaurant.delete()

    restaurantList = Restaurant.objects.all()
    return render(request, 'show_restaurant.html', {"restaurantList" : restaurantList})


def open_update_menu(request,restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    itemList = restaurant.items.all()
    return render(request,'update_menu.html', {"itemList":itemList, "restaurant":restaurant})

def update_menu(request,restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vegeterian = request.POST.get('vegeterian') == 'on'
        picture = request.POST.get('picture')

        try:
            Item.objects.get(name = name)
            return HttpResponse("Duplicate item!")
        except:
            Item.objects.create(
                restaurant = restaurant,
                name = name,
                description = description,
                price = price,
                vegeterian = vegeterian,
                picture = picture,
            )
    return render(request,'admin_home.html')       



def view_menu(request, restaurant_id, username):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    itemList = restaurant.items.all()
    #return HttpResponse("Items collected")
    #itemList = Item.objects.all()
    return render(request, 'customer_menu.html'
                  ,{"itemList" : itemList,
                     "restaurant" : restaurant, 
                     "username":username})

def add_to_cart(request, item_id, username):
    item = Item.objects.get(id = item_id)
    customer = user.objects.get(username = username)


    cart, created = Cart.objects.get_or_create(customer = customer)


    cart.items.add(item)


    return HttpResponse('added to cart')

def show_cart(request, username):
    customer = user.objects.get(username=username)
    cart = Cart.objects.filter(customer=customer).first()

    if cart:
        items = cart.items.all()
        total_price = cart.total_price()
    else:
        items = []
        total_price = 0

    return render(request, 'cart_item.html', {
        "itemlist": items,
        "total_price": total_price,
        "username": username
    })
def checkout(request, username):
    customer = get_object_or_404(user, username=username)
    cart = Cart.objects.filter(customer=customer).first()

    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'checkout.html', {
            'error': 'Your cart is empty!',
            'username': username
        })

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    order_data = {
        'amount': int(total_price * 100),
        'currency': 'INR',
        'payment_capture': '1',
    }

    order = client.order.create(data=order_data)

    return render(request, 'checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],
        'amount': int(total_price * 100),
    })
def orders(request, username):
    customer = get_object_or_404(user, username=username)

    # ✅ Get latest order
    order = Order.objects.filter(customer=customer).order_by('-created_at').first()

    return render(request, 'order.html', {
        'username': username,
        'order': order
    })
        
def order_history(request, username):
    customer = get_object_or_404(user, username=username)
    orders = Order.objects.filter(customer=customer).order_by('-created_at')

    return render(request, 'order_history.html', {
        'orders': orders,
        'username': username
    })
    
@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )

        try:
            # ✅ Verify payment
            client.utility.verify_payment_signature({
                'razorpay_order_id': data['razorpay_order_id'],
                'razorpay_payment_id': data['razorpay_payment_id'],
                'razorpay_signature': data['razorpay_signature']
            })

            # ✅ Get user
            customer = get_object_or_404(user, username=data['username'])
            cart = Cart.objects.filter(customer=customer).first()

            if not cart:
                return JsonResponse({'status': 'failed'})

            # ✅ CREATE ORDER (moved from your old view)
            order = Order.objects.create(
                customer=customer,
                total_price=cart.total_price()
            )

            # ✅ SAVE ITEMS
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    name=item.name,
                    price=item.price,
                    quantity=1
                )

            # ✅ CLEAR CART
            cart.items.clear()

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'failed'})