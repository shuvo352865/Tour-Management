"""tour_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tour import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('about/',views.About,name='about'),
    path('trips/',views.Trips,name='trips'),
    path('calculate/',views.Calculate,name='calculate'),
    path('aboutUs/',views.AboutUs,name='aboutUs'),
    path('tourmate-details/',views.Tourmate,name='tourmate-details'),
    path('travel/',views.Travel,name='travel'),
    path('hanif/',views.Hanif,name='hanif'),
    path('saintmartin/',views.Saintmartin,name='saintmartin'),
    path('shamoly/',views.Shamoly,name='shamoly'),
    path('greenline/',views.Greenline,name='greenline'),
    path('ena/',views.Ena,name='ena'),
    path('sohag/',views.Sohag,name='sohag'),
    path('sayman/',views.Sayman,name='sayman'),
    path('hotel/',views.Hotel,name='hotel'),
    path('seap/',views.Seap,name='seap'),
 path('jol/',views.Jol,name='jol'),
]
