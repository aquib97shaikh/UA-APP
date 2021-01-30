from django.shortcuts import render
from django.utils import timezone
from .models import User,UserLoginHistory
from rest_framework import generics, permissions
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
import jwt

@api_view(('POST',))
def register(request):
    if(request.method=="POST"):
        user = User.objects.filter(username=request.data["username"],password=request.data["password"]);
        if(len(user)>0):
            return Response({"success":False,"msg":"User already exists!"})
        user = User(username=request.data["username"],password=request.data["password"]);
        user.save();
        return Response({"success":True})
    return Response({"success":False})

@api_view(('POST',))
def login(request):
    if(request.method=="POST"):
        user = User.objects.filter(username=request.data["username"],password=request.data["password"]);
        if(len(user)>0):
            token = jwt.encode({"username":request.data["username"],"password":request.data["password"]},"SECRET", algorithm="HS256")
            ip = request.META.get('REMOTE_ADDR')
            user = user[0]
            userHistory = UserLoginHistory(user=user,loginAt=timezone.now())
            userHistory.save()
            # print({"user_id":user.id,"ip":ip})
            # print(userHistory)
            p = requests.post('https://encrusxqoan0b.x.pipedream.net/', params=request.POST,data={"user_id":user.id,"ip":ip})
            return Response({"success":"true","token":token})
    return Response({"success":"false"})

