from django.urls import path
from . views import Login_Api,Signup_Api,Cart_Api,Product_Api,Admin_Api,Message_Api,Home,Profile_Api,Categories_Api,Home_2,Request_Product,Rem_Cart,Account_Status,Logout,About,All,Remove_Product,Search_Api
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login', Login_Api.as_view(), name="login" ),
    path('signup', Signup_Api.as_view()),
    path('cart/<str:pk>', Cart_Api.as_view()),
    path('about/<str:pk>', About.as_view()),
    path('log/<str:pk>', Account_Status.as_view()),
    path('logout', Logout.as_view()),
    path('product/<str:pk>', Product_Api.as_view()),
    path('delete_cart', Rem_Cart.as_view()),
    path('sudo_admin', Admin_Api.as_view()),
    path('message/<str:pk>', Message_Api.as_view()),
    path('', Home.as_view()),
    path('get_more', All.as_view()),
    path('categories/<str:pk>', Categories_Api.as_view()),
    path('home/<str:pk>', Home_2.as_view(),),
    path('requested_product/<str:pk>/<str:pk2>', Request_Product.as_view()),
    path('profile', Profile_Api.as_view(), name="profile"),
    path('Rem_pro', Remove_Product.as_view(), name="profile"),
    path('Find', Search_Api.as_view()),



    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)