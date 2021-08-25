from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegister,UserUpdate,ProfileUpdate
from django.db.models import Q
from django.contrib import messages
from .models import Profile, Chat
from blogi.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.


def UserRegisterView(request):
    if(request.method == 'POST'):
        form = UserRegister(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'home/register.html', {'form': form})

def profile(request):
    if(request.method == 'POST'):
        user_form = UserUpdate(request.POST, instance=request.user)
        profile_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if(user_form.is_valid() and profile_form.is_valid()):
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Your information has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdate(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profile)

    return render(request, 'home/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def search_user_by_id(request):
    query = request.GET.get('uid')
    if(query):
        rezultatet = Profile.objects.filter(Q(user__username__icontains = query))
    elif(query==''):
        return redirect('home')
    else:
        return redirect('home')
    return render(request,"home/search.html",{'search':rezultatet})

def get_profile(request, pk):
    template = "home/users_profiles.html"
    profilet = Profile.objects.filter(user = pk)

    friend = get_object_or_404(Profile,  user=pk)
    current_user = get_object_or_404(Profile,  user__username=request.user)
    is_friended = False
    if(current_user.friends.filter(id=friend.user.id).exists()):
        is_friended = True

    return render(request,"home/users_profiles.html",{'profilet':profilet,'is_friended':is_friended})

@login_required(redirect_field_name='home/home.html')
def add_friends(request, pk):
    friend = get_object_or_404(Profile,  id=pk)
    print(friend)
    current_user = get_object_or_404(Profile,  user__username=request.user)
    print("current user", current_user)
    is_friended = False
    if(current_user.friends.filter(id=friend.user.id).exists()):
        print('ok', friend.id)
        current_user.friends.remove(friend.user.id)
        friend.followers.remove(request.user)
        is_friended = False
    else:
        print('ok', friend.id)
        current_user.friends.add(friend.user.id)
        friend.followers.add(request.user)
        is_friended = True
        messages.success(request, f'You started following {friend.user}! You will now be able to see what {friend.user} shares in your Timeline!')
    return redirect('/profile-users/' + str(friend.user.id))

    return render(request,"home/users_profiles.html",{"friend":current_user})

@login_required(redirect_field_name='home/home.html')
def remove_followers(request, pk):
    friend = get_object_or_404(Profile,  id=pk)
    print(friend)
    current_user = get_object_or_404(Profile,  user__username=request.user)
    print("current user", current_user)
    if(current_user.followers.filter(id=friend.user.id).exists()):
        print('ok', friend.user.id)
        current_user.followers.remove(friend.user.id)
        friend.friends.remove(request.user)
    return redirect('/user-followers/' + str(current_user.id))

    return render(request,"home/users_followers.html",{"remove":friend})

def timeline(request):
    profile = Profile.objects.get(user__username=request.user)
    print(profile)
    friends = profile.friends.all()
    # your_posts = Post.objects.filter(autori = request.user).order_by('-koha_posti')
    friend_posts = Post.objects.filter(autori__in = friends).order_by('-koha_posti')
    print(friend_posts)
   
    return render(request,"blogi/timeline.html",{"friend_posts":friend_posts})

def home(request):
    c = Chat.objects.all()
    return render(request, "home/home.html", {'home': 'active', 'chat': c})

def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        print(c)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')

def message(request):
    c = Chat.objects.all()
    return render(request, 'home/messages.html', {'chat': c})


def get_friends(request, pk):
    user = get_object_or_404(Profile,  id=pk)
    user_friends = user.friends.all()
    print(user_friends)

    return render(request,"home/users_friends.html",{'user_friends':user_friends})

def get_followers(request, pk):
    user = get_object_or_404(Profile,  id=pk)
    user_followers = user.followers.all()
    print(user_followers)

    return render(request,"home/users_followers.html",{'user_followers':user_followers})
