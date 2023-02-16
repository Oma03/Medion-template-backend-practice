from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Medicine, Vitamins, Contacts
from django.contrib import messages

# Create your views here.


def home(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone Number')
        message = request.POST.get('Message')
        med = request.POST.get('Select medicine')
        contacts = Contacts(name=name, phone=phone, email=email, t_o_m=med, message=message,)
        contacts.save()
        messages.success(request, 'Message saved successfully, thank you')

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/index.html', context)


def about(request):
    return render(request, 'please/about.html')


def medicine(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()
    context = {
        "all_products": all_products,
        "one_product": one_product
    }
    return render(request, 'please/medicine.html', context)


def buy(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/buy.html', context)


def news(request):
    return render(request, 'please/news.html')


def contact(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        med = request.POST.get('med')
        contacts = Contacts(name=name, phone=phone, email=email, t_o_m=med, message=message,)
        contacts.save()
        messages.success(request, 'Feedback Received')

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/contact.html', context)


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'please/login1.html')
        else:
            messages.error(request, "Password or Username incorrect")
            return render(request, 'please/login.html')
    else:
        return render(request, 'please/login.html')


def login1(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()
    context = {
        "all_products": all_products,
        "one_product": one_product
    }
    return render(request, 'please/login1.html', context)


def new(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['name'])
                messages.error(request, 'Username is already taken!')
                return render(request, 'please/new.html')
            except:
                user = User.objects.create_user(request.POST['name'], password=request.POST['password'], email=
                                                request.POST['email'])
                messages.success(request, 'Details saved successfully, thank you')
                auth.login(request, user)
                return render(request, 'please/login1.html')
        else:
            messages.error(request, 'Password does not match!')
            return render(request, 'please/new.html')
    else:
        return render(request, 'please/new.html')


def payment(request, pk):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    if request.method == 'POST':
        if len(request.POST['card_no']) == 16:
            if len(request.POST['pin']) == 4:
                if len(request.POST['cvv']) == 3:
                    messages.success(request, 'Item Paid for!! Enjoy')
                else:
                    messages.error(request, 'Wrong cvv')
            else:
                messages.error(request, 'Wrong pin')
        else:
            messages.error(request, 'Wrong Card number')

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/payment.html', context)


def medicine1(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()
    context = {
        "all_products": all_products,
        "one_product": one_product
    }
    return render(request, 'please/medicine1.html', context)


def buy1(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/buy1.html', context)


def news1(request):
    return render(request, 'please/news1.html')


def contact1(request):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        med = request.POST.get('med')
        contacts = Contacts(name=name, phone=phone, email=email, t_o_m=med, message=message,)
        contacts.save()
        messages.success(request, 'Feedback Received')

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/contact1.html', context)


def payment1(request, pk):
    all_products = Medicine.objects.all()
    one_product = Vitamins.objects.all()

    if request.method == 'POST':
        if len(request.POST['card_no']) == 16:
            if len(request.POST['pin']) == 4:
                if len(request.POST['cvv']) == 3:
                    messages.success(request, 'Item Paid for!! Enjoy')
                else:
                    messages.error(request, 'Wrong cvv')
            else:
                messages.error(request, 'Wrong pin')
        else:
            messages.error(request, 'Wrong Card number')

    context = {
        "all_products": all_products,
        "one_product": one_product
    }

    return render(request, 'please/payment1.html', context)