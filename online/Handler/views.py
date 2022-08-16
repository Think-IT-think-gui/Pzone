from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ClientInfoSerializer,SignUpSerializer,CartSerializer,ProductSerializer,AdminSerializer,MessageSerializer
from . models import Login_info,SignUp_info,Cart_info,Products,Admin,Contact
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import sqlite3
from pathlib import Path
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from time import *
import uuid
from django.core.files.storage import FileSystemStorage
import os
from django.shortcuts import render,get_object_or_404
from django.db.models import Q

#============================================User name and password===========================================
BASE_DIR = Path(__file__).resolve().parent.parent
class Login_Api(APIView):
    global Clients_info
    def get(self, request):
        
        Recieved_data = Login_info.objects.all()
        serializer = ClientInfoSerializer(Recieved_data, many=True)
        return render(request, 'Login.html') 
    def post(self, request):    
          serializer = ClientInfoSerializer(data=request.data)  
          if serializer.is_valid():
            user1_check = request.data['User']
            user2_check = request.data['Password']          
            conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{user1_check}'")
            Clients_info = c.fetchone()
            conn1.commit()
            conn1.close()  
            if Clients_info == None:               
               return render(request, 'errors/invalid_credentials.html')  
            else:
              print(Clients_info)  
              if Clients_info[5] == user2_check: 
                print("hi")  
                conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
                c = conn1.cursor()
                c.execute(f"SELECT * FROM  Handler_Products")
                product_info = c.fetchmany(10)
                conn1.commit()
                conn1.close()  
                serializer.save() 
               # user = models.SignUp_info.objects.filter(request, username=user1_check ,password=user2_check)
               # print (user)
               # if user is not None:
                # login(request, user) 
               # Response("data").set_cookie('User','val')
              #  value = request.COOKIES.get('User')
             #   print(value)
                return render(request, 'main.html', {'product':product_info, 'User':user1_check,'roll':product_info}) 
               # else:    
              else:
                 return render(request, 'errors/invalid_credentials.html')             
          return Response("Error3") 

class Account_Status(APIView):
    def get(self, request, pk):
        if pk ==  "user1_check": 
          return redirect('login')
        else:
          return render(request,'logout.html', {"User":pk})   


class Logout(APIView):
    def post(self, request):

       conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
       c = conn1.cursor()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info = c.fetchall()
       conn1.commit()
       conn1.close()  
       return render(request, 'main.html', {'product':product_info, 'User':"user1_check" ,'roll':product_info})    

#============================================User name and password===========================================


#=============================================== create account =================================================
class Home(APIView):
    def get(self , request):
       conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
       c = conn1.cursor()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info = c.fetchmany(10)
       conn1.commit()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info2 = c.fetchmany(6)
       conn1.commit()
       conn1.close() 
       
    #   print(product_info2)
       return render(request, 'main.html', {'product':product_info, 'User':"user1_check" ,'roll':product_info2}) 

class All(APIView):
    def post(self , request):
       conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
       c = conn1.cursor()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info = c.fetchall()
       conn1.commit()
       c = conn1.cursor()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info2 = c.fetchmany(6)
       conn1.commit()
       conn1.close()  

       return render(request, 'main.html', {'product':product_info, 'User':request.data["User"] ,'roll':product_info2}) 

class About(APIView):
    def get(self , request, pk):
       
       return render(request, 'about.html', { 'User':pk}) 

class Signup_Api(APIView):
    def get(self, request):
        Recieved_data = SignUp_info.objects.all()
        serializer = SignUpSerializer(Recieved_data, many=True) 
        
        #return Response(serializer.data)
        return render(request, 'Signup.html') 
    def post(self, request):  
        user1_check = request.data["User"] 
        serializer = SignUpSerializer(data=request.data)
        print(serializer) 
        if serializer.is_valid():
         conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{user1_check}'")
         Clients_info = c.fetchone()
         conn1.commit()
         conn1.close()
         if Clients_info == None:     
          serializer.save()  
          return render(request, 'Profile_img.html', {'user':request.data["User"]}) 
         else:
          return render(request, 'errors/Already_exist.html')    
        return render(request, 'errors/Input_error.html') 
         #return render(request, 'Error_page/error_page.html')

class Categories_Api(APIView):
    def get(self, request, pk):
        print(request.data)
        return render(request, 'services.html', {'User':pk} ) 

class Request_Product(APIView):
    def get(self, request, pk, pk2):
        print(request.data)
        #return Response(pk+pk2)
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Products WHERE  Class='{pk2}' ")
        product_info = c.fetchall()
        print(product_info)
        conn1.commit()
        conn1.close()
        if product_info == []:
            data = f"No items found in {pk2}"
        else:
           data = f"Products of {pk2}"     
        return render(request, 'request_data.html', {'product':product_info, 'User':pk , 'stat':data}) 

class Home_2(APIView):
    def get(self, request, pk):
       conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
       c = conn1.cursor()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info = c.fetchmany(10)
       conn1.commit()
       c.execute(f"SELECT * FROM  Handler_Products")
       product_info2 = c.fetchmany(6)
       conn1.commit()
       conn1.close()  
       return render(request, 'main.html', {'product':product_info, 'User':pk ,'roll':product_info2}) 


class Profile_Api(APIView):

    def get(self, request):
        Recieved_data = SignUp_info.objects.all()
        pass
    def post(self, request): 
         print(request.data["User"])   
         uploading_file = request.FILES['Img']
         fs = FileSystemStorage()  
         old = uploading_file.name
         file_path2 = str(request.data['User']+'.jpg').replace(" ","")
         fs.save("Clients//"+request.data['User']+".jpg",uploading_file)
         conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
         c = conn1.cursor()
         c.execute(f"""UPDATE Handler_Signup_info SET Img = :img WHERE User = :user """,{'img':request.data['User'],'user':request.data['User']})
         conn1.commit()
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_Products")
         product_info = c.fetchmany(10)
         conn1.commit()
         c.execute(f"SELECT * FROM  Handler_Products")
         product_info2 = c.fetchmany(6)
         conn1.commit()
         conn1.close()   
         return render(request, 'main.html', {'product':product_info, 'User':request.data['User'] ,'roll':product_info2}) 
 
                
#=============================================== create account =================================================


#=============================================== create cart =================================================

class Rem_Cart(APIView):
    def post(self, request):
        user = request.data["User"]
        product = request.data["Product"]
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"DELETE from  Handler_Cart_info WHERE Product='{product}'")
        conn1.commit()
        c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{user}'")
        info = c.fetchall()
        print(product)
        conn1.commit()
        conn1.close()  
        return render(request, 'cart.html' ,{'User':user, 'cart':info})

class Cart_Api(APIView):
    def get(self, request, pk):
        if pk == "user1_check":
            return redirect('login')
        Recieved_data = Cart_info.objects.all()
        serializer = CartSerializer(Recieved_data, many=True)
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{pk}'")
        info = c.fetchall()
        conn1.commit()
        conn1.close()  
        return render(request, 'cart.html' ,{'User':pk, 'cart':info})
    def post(self, request, pk):  
        serializer = CartSerializer(data=request.data)
        user = request.data["User"]
        if serializer.is_valid():
         if request.data["User"] ==  "user1_check": 
          return redirect('login')
         else:
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{user}'")
          data = c.fetchall()
          conn1.commit()
          conn1.close()
          for i in data:
              if request.data["Product"] == i[1]:
                   conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
                   c = conn1.cursor()
                   c.execute(f"SELECT * FROM  Handler_Products")
                   product_info = c.fetchmany(10)
                   conn1.commit()
                   c.execute(f"SELECT * FROM  Handler_Products")
                   product_info2 = c.fetchmany(6)
                   conn1.commit()
                   conn1.close() 
                   return render(request, 'main.html', {'product':product_info, 'User':request.data["User"],'roll':product_info2}) 
              else:
                   pass
          serializer.save()  
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Products")
          product_info = c.fetchmany(10)
          conn1.commit()
          c.execute(f"SELECT * FROM  Handler_Products")
          product_info2 = c.fetchmany(6)
          conn1.commit()
          conn1.close() 
          return render(request, 'main.html', {'product':product_info, 'User':request.data["User"],'roll':product_info2}) 
        return Response("Error") 
        

                
#=============================================== create cart =================================================


#=============================================== products =================================================

class Product_Api(APIView):
    
    def post(self, request, pk): 
        pro = request.data["Product"]
        serializer = ProductSerializer(data=request.data)  
        print(serializer) 
        if serializer.is_valid():

         conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')       
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_Products WHERE Product='{pro}'")
         Pro_info = c.fetchall()
         conn1.commit()
         conn1.close()
         print(Pro_info)
         if Pro_info == []:
          serializer.save()
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3') 
          uploading_file = request.FILES['Img']
          fs = FileSystemStorage()  
          old = uploading_file.name
          file_path = str(old).split('_')
          file_path2 = (repr(file_path[-1])).replace("'","")[0:-4]
          fs.save("Product//"+request.data['Product']+".jpg",uploading_file)      
         else:
             pass
         conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')   
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_SignUp_info")
         Clients_info = c.fetchall()
         conn1.commit()
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_Products")
         Pro_info = c.fetchall()
         conn1.commit()
         conn1.close() 

         return render(request, 'Admin_Tab/index.html', {"User":pk,"Info":Clients_info, "Product":Pro_info})
              
         return Response(serializer.data)

        
class Search_Api(APIView):

    def post(self, request):
        Recieved = request.data["LookFor"]
        data = Products.objects.filter(Q(Product__icontains=Recieved))
        if str(data) == "<QuerySet []>":
         tell="No result found!"   
         return render(request, 'search.html', {"User":request.data["User"],"Info":[],"comment":tell})
        else:
         tell=f"Search result of '{Recieved}'"   
         Result = [] 
         for i in data:       
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')   
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Products WHERE Product='{i}' ")
          Pro_info = c.fetchone()
          conn1.commit()
          conn1.close()
          Result.append(Pro_info)
        return render(request, 'search.html', {"User":request.data["User"],"Info":Result,"comment":tell})

      
#=============================================== products =================================================

#=============================================== Admin account =================================================

class Admin_Api(APIView):

    def get(self, request):
        Recieved_data = Admin.objects.all()
        serializer = AdminSerializer(Recieved_data, many=True) 
        #return Response(serializer.data)
        return render(request, 'Admin_Tab/data.html')
    def post(self, request):    
            serializer = AdminSerializer(data=request.data) 
            user1_check = request.data['User']
            user2_check = request.data['Password']    
            conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_Admin WHERE  User='{user1_check}'")
            Clients_info = c.fetchone()
            print(Clients_info)
            conn1.commit()
            conn1.close()  
            if Clients_info == None:               
               return render(request, 'errors/invalid_credentials.html')  
            else:
             if Clients_info[2] == user2_check: 
                 conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
                 c = conn1.cursor()
                 c.execute(f"SELECT * FROM  Handler_SignUp_info")
                 Clients_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute(f"SELECT * FROM  Handler_Products")
                 Pro_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute(f"SELECT * FROM  Handler_Contact")
                 msg_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute(f"SELECT * FROM  Handler_Login_info")
                 log_info = c.fetchall()
                 conn1.commit()
                 conn1.close()  
                 return render(request, 'Admin_Tab/index.html', {"User":user1_check,"Info":Clients_info, "Product":Pro_info, "ask":msg_info, "logs":log_info})
             else:
                 
                 return render(request, 'errors/invalid_credentials.html')  



class Remove_Product(APIView):
    def post(self, request):  
            print(request.data)
            product = request.data["Product"]      
            conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
            c = conn1.cursor()
            c.execute(f"DELETE from  Handler_Products WHERE Product='{product}'")
            conn1.commit()
            os.remove(f"{BASE_DIR}//static//media//product//{product}.jpg")
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info")
            Clients_info = c.fetchall()
            conn1.commit()
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_Products")
            Pro_info = c.fetchall()
            conn1.close()  
            return render(request, 'Admin_Tab/index.html', {"User":request.data["User"],"Info":Clients_info, "Product":Pro_info})
            
                
#=============================================== Admin account =================================================


#=============================================== messages =================================================

class Message_Api(APIView):

    def get(self, request, pk):
        Recieved_data = Contact.objects.all()
        serializer = MessageSerializer(Recieved_data, many=True) 
        return render(request, 'contact.html', {'User':pk}) 

    def post(self, request, pk):    
        serializer = MessageSerializer(data=request.data) 
        if serializer.is_valid():
          serializer.save()  
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Products")
          product_info = c.fetchmany(10)
          conn1.commit()
          c.execute(f"SELECT * FROM  Handler_Products")
          product_info2 = c.fetchmany(6)
          conn1.commit()
          conn1.close()   
          return render(request, 'main.html', {'product':product_info, 'User':pk,'roll':product_info2}) 


                
#=============================================== messages =================================================
