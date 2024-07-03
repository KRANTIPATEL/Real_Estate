from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import  get_object_or_404
from homeproperty.models import Home_Property
from django.contrib import messages
from django.contrib.sessions.models import Session
from UserData.models import User
from django.contrib.auth.hashers import make_password
from MainpropertyData.models import Mainproperty 


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        count = User.objects.filter(email=email, password=password).count()
        if count > 0:
            request.session['is_login'] = True
            return redirect('home')
        else:
            messages.error(request, "Wrong email or password", extra_tags='login')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.session.get('is_login'):
        return redirect('home')
    
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            messages.error(request, "Password and Confirm Password should be the same", extra_tags='signup')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists", extra_tags='signup')
            return render(request, 'signup.html')

        user = User(username=f'{firstname} {lastname}', email=email, password=password)
        user.save()
        messages.success(request, "Registration Done", extra_tags='signup')
        return redirect('login')

    return render(request, 'signup.html')

def registeruser(request):
    

    return HttpResponse("data insert done")

   

def property(request):
    return render(request,'property.html')


def property2(request):
    return render(request,'property2.html')


def property3(request):
    return render(request,'property3.html')


def property4(request):
    return render(request,'property4.html')


def property5(request):
    return render(request,'property5.html')


# def home1(request):
#     if request.session.has_key('is_login'):
#         return render(request,'home.html')
#     else:
#         return render('login.html')

def home(request):
        
    homeData = Home_Property.objects.all()

    if 'is_login' in request.session and request.session['is_login']:

        return render(request, 'home.html',{'homeData':homeData})
    else:
        return redirect('login')



def mainproperty(request):

    if request.session['is_login']:

        if request.method == "POST":
            pt = request.POST['search']

        if pt!= None:
            mainproperty =  Home_Property.objects.filter(location__icontains = pt)

        return render(request, "mainproperty.html",{'mainproperty':mainproperty})
    else:
        return render(request, 'login.html')

def property_detail(request, id):
    property = get_object_or_404(Home_Property, id=id)
    return render(request, 'property_detail.html', {'property': property})

def search(request):
    if request.session['is_login']:
        return render(request,'mainproperty.html')
    else:
        return render(request, 'login.html')


def header(request):
    if request.session['is_login']:
    
        return render(request,'header.html')
    else:
        return render(request, 'login.html')


def services(request):
    # if request.session['is_login']:
    #     if request.POST:
    #         FullName = request.POST['FullName']
    #         email = request.POST['email']
    #         City = request.POST['City']
    #         message = request.POST['message']
    #         ApartmentSize = request.POST['ApartmentSize']
    #         obj =Service(FullName=FullName,email=email,City=City,message=message,ApartmentSize=ApartmentSize)
    #         obj.save()
    #         return HttpResponse("Enquiry sent. You will Recive Enquiry by admin within 2 days")
    # else:
    #     return render(request, 'login.html')
    return render(request, 'services.html')

def footer(request):
    if request.session['is_login']:

        return render(request,'footer.html')
    else:
        return render(request, 'login.html')

def contactus(request):
    # if request.session['is_login']:

    #     if request.POST:
    #         Firstname = request.POST['Firstname']
    #         Lastname = request.POST['Lastname']
    #         email = request.POST['email']
    #         subject = request.POST['subject']
    #         message = request.POST['message']
    #         obj = Contactus(Firstname=Firstname,Lastname=Lastname, email=email, subject=subject,message=message)
    #         obj.save()
    #         messages.success(request, "Message sent")
    # else: 
    #     return render(request, 'login.html')

    return render(request, 'contactus.html')

def contactagent(request):
    if request.session['is_login']:
        return render(request,'contactagent.html')
    else: 
        return render(request, 'login.html')
    

def logout(request):
    request.session['is_login'] = False
    return redirect('login')


def Calc(request):
    # if request.session['is_login']:
        return render(request,'Calc.html')
    # else:
        # return render(request, 'login.html')
