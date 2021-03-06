import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import *


def index(request):
    if request.POST:
        res = request.POST['post-body']
        post = Post(user=request.user, body=res, )
        post.save()

    posts = Post.objects.all().order_by('-pk')
    per_page = 10
    p = Paginator(posts, per_page)
    pageNum=1
    page = p.page(pageNum)
    
    page_range = p.page_range

    if page.has_next() == True:
        pNext = ''
    else:
        pNext = 'd-none'
    
    if page.has_previous() == True:
        pPrevious = ''
    else:
        pPrevious = 'd-none'

    post = page.object_list
    
    context = {'posts': post, 'pNext':pNext, 'pPrevious':pPrevious, 'page_range':page_range, 'current_page':pageNum}
    return render(request, "network/index.html", context)
    
def page(request, pg):
    if request.POST:
        res = request.POST['post-body']
        post = Post(user=request.user, body=res, )
        post.save()

    posts = Post.objects.all().order_by('-pk')
    per_page = 10
    p = Paginator(posts, per_page)
    pageNum=pg
    page = p.page(pageNum)
    page_range = p.page_range

    if page.has_next() == True:
        pNext = ''
    else:
        pNext = 'd-none'
    
    if page.has_previous() == True:
        pPrevious = ''
    else:
        pPrevious = 'd-none'

    post = page.object_list
    
    context = {'posts': post, 'pNext':pNext, 'pPrevious':pPrevious, 'page_range':page_range, 'current_page':pageNum}
    return render(request, "network/index.html", context)

def get_post(request, id):
    post = Post.objects.filter(pk=id)
    for x in post:
        body = x.body
        return JsonResponse({"body":body}, status=200)


@csrf_exempt
def update_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('post_id') is not None:
            id = data.get('post_id')
            edited_post = data.get('edited_post')
            post = Post.objects.filter(pk=id)
            for post in post:
                post.body = edited_post
                post.save()
                body = post.body

                return JsonResponse({"body":body}, status=200)


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
    if data.get('post_id') is not None:
        action = data.get('action')
        post_id = data.get('post_id')
        if action == 'like':
            dislike = Dislike.objects.filter(user=request.user, post=post_id).count()
            if dislike > 0:
                l = Dislike.objects.filter(user=request.user, post=post_id)
                l.delete()

                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalDislikes = int(post.totalDislikes) - 1
                    post.save()

            like = Like.objects.filter(user=request.user, post=post_id).count()
            if like > 0:
                l = Like.objects.filter(user=request.user, post=post_id)
                l.delete()
            
                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalLikes = int(post.totalLikes) - 1
                    post.save()
                
                totalLikes = post.totalLikes
                totalDislikes = post.totalDislikes
                return JsonResponse({"totalLikes":totalLikes, 'totalDislikes':totalDislikes}, status=200)
            else:
                l = Like(user=request.user, post=Post.objects.get(pk=post_id))
                l.save()
            
                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalLikes = int(post.totalLikes) + 1
                    post.save()

                totalLikes = post.totalLikes
                totalDislikes = post.totalDislikes
                return JsonResponse({"totalLikes":totalLikes, 'totalDislikes':totalDislikes}, status=200)
        elif action == 'dislike':
            like = Like.objects.filter(user=request.user, post=post_id).count()
            if like > 0:
                l = Like.objects.filter(user=request.user, post=post_id)
                l.delete()
            
                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalLikes = int(post.totalLikes) - 1
                    post.save()

            dislike = Dislike.objects.filter(user=request.user, post=post_id).count()
            if dislike > 0:
                l = Dislike.objects.filter(user=request.user, post=post_id)
                l.delete()

                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalDislikes = int(post.totalDislikes) - 1
                    post.save()

                totalLikes = post.totalLikes
                totalDislikes = post.totalDislikes
                return JsonResponse({"totalLikes":totalLikes, 'totalDislikes':totalDislikes}, status=200)
            
            else:
                l = Dislike(user=request.user, post=Post.objects.get(pk=post_id))
                l.save()
            
                post = Post.objects.filter(pk=post_id)
                for post in post:
                    post.totalDislikes = int(post.totalDislikes) + 1
                    post.save()

                totalLikes = post.totalLikes
                totalDislikes = post.totalDislikes
                return JsonResponse({"totalLikes":totalLikes, 'totalDislikes':totalDislikes}, status=200)
            
        return HttpResponse('error')
    
    # do something like below where you'll check if rUser has dislike and wants to like; firstly remove the dislike and add a like
    # update both like table and totalLikes in post table


def profile(request, user_id, pg):
    # user_id is actuall username please
    if request.user.is_authenticated:

        follower = Follower.objects.filter(user=User.objects.get(username=user_id)).count()
        following = Follower.objects.filter(follower=User.objects.get(username=user_id)).count()

        f = Follower.objects.filter(user=User.objects.get(username=user_id), follower=request.user).count()
        
        posts = Post.objects.filter(user=User.objects.get(username=user_id)).order_by('-pk')
        
        per_page = 10
        p = Paginator(posts, per_page)
        pageNum=pg
        page = p.page(pageNum)
        page_range = p.page_range
    
        if page.has_next() == True:
            pNext = ''
        else:
            pNext = 'd-none'
        
        if page.has_previous() == True:
            pPrevious = ''
        else:
            pPrevious = 'd-none'
    
        post = page.object_list
        
        context = {'posts': post, 'following':following, 'follower':follower, 'pUser':user_id, 'f':f, 'pNext':pNext, 'pPrevious':pPrevious, 'page_range':page_range, 'current_page':pageNum}
        return render(request, "network/profile.html", context)

    return HttpResponseRedirect(reverse("login"))


@csrf_exempt
def follow(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('pUser') is not None:
            pUser = data.get('pUser')
            action = data.get('action')

            if action == 'follow':
                follow = Follower(user=User.objects.get(username=pUser), follower= request.user)
                follow.save()
                print('success')

                return JsonResponse({"message":'success'}, status=200)

            elif action == 'unfollow':
                unfollow = Follower.objects.filter(user=User.objects.get(username=pUser), follower= request.user)
                unfollow.delete()
                print('success')

                return JsonResponse({"message":'success'}, status=200)


def following(request, pg):
    if request.user.is_authenticated:
        
        # select * from post where user = (select user from follower where user = request.user)
        posts = Post.objects.filter(user__following__follower=request.user.id).order_by('-pk')
        
        per_page = 10
        p = Paginator(posts, per_page)
        pageNum=pg
        page = p.page(pageNum)
        page_range = p.page_range
    
        if page.has_next() == True:
            pNext = ''
        else:
            pNext = 'd-none'
        
        if page.has_previous() == True:
            pPrevious = ''
        else:
            pPrevious = 'd-none'
    
        post = page.object_list
        
        context = {'posts': post, 'pNext':pNext, 'pPrevious':pPrevious, 'page_range':page_range, 'current_page':pageNum}
        return render(request, "network/following.html", context)

    return HttpResponseRedirect(reverse("login"))