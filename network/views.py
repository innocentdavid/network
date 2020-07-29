import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *


def index(request):
    if request.POST:
        res = request.POST['post-body']
        post = Post(user=request.user, body=res)
        post.save()

    posts = Post.objects.all().order_by('-pk')
    x = Post.objects.all()
    for x in x:
        f = Follower.objects.filter(user=x.user, follower=request.user).count()

        context = {'posts': posts, 'f': f}
        return render(request, "network/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
@csrf_exempt
@login_required
def vote(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    post_id = data.get('post_id')
    print(post_id)
    return HttpResponse('error')
    
    # do something like below where you'll check if rUser has dislike and wants to like; firstly remove the dislike and add a like
    # update both like table and totalLikes in post table


    # try:
    #     email = Email.objects.get(user=request.user, pk=email_id)
    # except Email.DoesNotExist:
    #     return JsonResponse({"error": "Email not found."}, status=404)

    # # Return email contents
    # if request.method == "GET":
    #     return JsonResponse(email.serialize())

    # # Update whether email is read or should be archived
    # elif request.method == "PUT":
    #     data = json.loads(request.body)
    #     if data.get("read") is not None:
    #         email.read = data["read"]
    #     if data.get("archived") is not None:
    #         email.archived = data["archived"]
    #     email.save()
    #     return HttpResponse(status=204)

    # # Email must be via GET or PUT
    # else:
    #     return JsonResponse({
    #         "error": "GET or PUT request required."
    #     }, status=400)
