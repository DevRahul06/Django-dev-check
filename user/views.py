from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    client = Clientlogo.objects.all()
    return render(request,'dashboard.html',{'client':list(client)})

def vehicle_magnet(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_magnet.html', {'vehicle': vehicles})

# method for dropdown menu paperprint

def businesscard(request):
    return render(request,'paperprint/businesscard.html')
def flyers(request):
    return render(request,'paperprint/flyers.html')
def postcard(request):
    return render(request,'paperprint/postcard.html')
def brochures(request):
    return render(request,'paperprint/brochures.html')
def doorhanger(request):
    return render(request,'paperprint/doorhanger.html')
def paperprint(request):
    return render(request,'paperprint.html')
    

# method for dropdown menu Banner

def vinylbanner(request):
    return render(request,'banner/vinylbanner.html')
def meshbanner(request):
    return render(request,'banner/meshbanner.html')
def fabricbanner(request):
    return render(request,'banner/fabricbanner.html')
def rollupbanner(request):
    return render(request,'banner/rollupbanner.html')
def backlitbanner(request):
    return render(request,'banner/backlitbanner.html')

# method for dropdown menu Flag

def angledflag(request):
    return render(request, 'flag/angledflag.html')

def convexflag(request):
    return render(request, 'flag/convexflag.html')

def rectangleflag(request):
    return render(request, 'flag/rectangleflag.html')

def poleflag(request):
    return render(request, 'flag/poleflag.html')
# method for dropdown menu Truck / decals

def decal(request):
    return render(request, 'truck/decal.html')

def sticker(request):
    return render(request, 'truck/sticker.html')

# method for dropdown menu windowsign
def adhesivevinyl(request):
    return render(request, "windowsign/adhesivevinyl.html")

def perfratvinyl(request):
    return render(request, "windowsign/perfratvinyl.html")

def threemvinyl(request):
    return render(request, "windowsign/threemvinyl.html")

def windowclingvinyl(request):
    return render(request, "windowsign/windowclingvinyl.html")

def translucentvinyl(request):
    return render(request, "windowsign/translucentvinyl.html")

def clearvinyl(request):
    return render(request, "windowsign/clearvinyl.html")

# for 3D letter
def nonled(request):
    return render(request, "3dletter/nonled.html")

def channellatter(request):
    return render(request, "3dletter/channellatter.html")
#for property sign

def yardsigns(request):
    return render(request, "propertysigns/yardsigns.html")

def framestandi(request):
    return render(request, "propertysigns/framestandi.html")

def aluminum(request):
    return render(request, "propertysigns/aluminum.html")

def postsigns(request):
    return render(request, "propertysigns/postsigns.html")

def pylonsigns(request):
    return render(request, "propertysigns/pylonsigns.html")
