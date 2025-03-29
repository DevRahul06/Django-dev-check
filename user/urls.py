from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('vehicle_magnet', views.vehicle_magnet, name="vehicle_magnet"),
    # urls for dropdown menu Paper print
    path('businesscard',views.businesscard,name="businesscard"),
    path('flyers',views.flyers,name="flyers"),
    path('postcard',views.postcard,name="postcard"),
    path('brochures',views.brochures,name="brochures"),
    path('doorhanger',views.doorhanger,name="doorhanger"),
    # urls for dropdown menu Paper print
    path('vinylbanner',views.vinylbanner,name="vinylbanner"),
    path('meshbanner',views.meshbanner,name="meshbanner"),
    path('fabricbanner',views.fabricbanner,name="fabricbanner"),
    path('rollupbanner',views.rollupbanner,name="rollupbanner"),
    path('backlitbanner',views.backlitbanner,name="backlitbanner"),
    # urls for dropdown menu flag
    path('angledflag', views.angledflag, name="angledflag"),
    path('convexflag', views.convexflag, name="convexflag"),
    path('rectangleflag', views.rectangleflag, name="rectangleflag"),
    path('poleflag', views.poleflag, name="poleflag"),
    # urls for dropdown menu Truck / Decalse
    path('decal', views.decal, name="decal"),
    path('sticker', views.sticker, name="sticker"),

    # urls for dropdown window signs
    path('adhesivevinyl', views.adhesivevinyl, name="adhesivevinyl"),
    path('perfratvinyl', views.perfratvinyl, name="perfratvinyl"),
    path('threemvinyl', views.threemvinyl, name="threemvinyl"),
    path('windowclingvinyl', views.windowclingvinyl, name="windowclingvinyl"),
    path('translucentvinyl', views.translucentvinyl, name="translucentvinyl"),
    path('clearvinyl', views.clearvinyl, name="clearvinyl"),
    path('paperprint',views.paperprint,name="paperprint"),

    # for 3D letter
    path('nonled', views.nonled, name="nonled"),
    path('channellatter', views.channellatter, name="channellatter"),
    #for property sign
    path('yardsigns', views.yardsigns, name="yardsigns"),
    path('framestandi', views.framestandi, name="framestandi"),
    path('aluminum', views.aluminum, name="aluminum"),
    path('postsigns', views.postsigns, name="postsigns"),
    path('pylonsigns', views.pylonsigns, name="pylonsigns"),



    

    

    
    
]
