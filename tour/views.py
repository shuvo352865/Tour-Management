from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


def About(request):
    return render (request,'about.html')

def Trips(request):
        return render (request,'trips.html')  


def Calculate(request):
        return render (request,'calculate.html')  

def AboutUs(request):
        return render (request,'aboutUs.html')  

def Hotel(request):
        return render (request,'hotel.html')  
def Tourmate(request):
        return render (request,'tourmate-details.html')  
def Travel(request):
        return render (request,'travel.html')  
def Hanif(request):
        return redirect ("https://www.hanif-enterprise.com") 
def Saintmartin(request):
        return redirect ("https://saintmartinparibahanbd.com/")  

def Shamoly(request):
        return redirect ("https://www.shyamoliparibahan-bd.com") 
def Ena(request):
        return redirect ("https://www.bookaway.com/suppliers/ena-paribahan")  
def Greenline(request):
        return redirect ("https://greenlinebd.com/") 

def Sohag(request):
        return redirect ("https://shohagh.com/") 
def Sayman(request):
        return redirect ("https://sayemanresort.com") 
def Seap(request):
        return redirect ("https://www.seapearlcoxsbazar.com/") 
def Jol(request):
        return redirect ("https://www.joltorongo.com.bd") 
def LogoutPage(request):
    logout(request)
    return redirect('login') 