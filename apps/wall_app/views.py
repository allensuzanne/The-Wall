from django.shortcuts import render, redirect
from .models import Message, Comment
from ..login_app.models import User
import datetime

def wall(request):
    print('*'*80)
    context = {
        'message_list': Message.objects.all().order_by('-updated_at'),
        'user_name' : User.objects.get(id=request.session['user_id']),
    }
    return render(request, "wall_app/wall.html", context)

def messages(request):
    print('*'*80)
    user_id=User.objects.get(id=request.session['user_id'])
    Message.objects.create(message=request.POST['messages'], user=user_id)
    return redirect('/wall')


def comments(request): 
    print('*'*80)
    user_id=User.objects.get(id=request.session['user_id'])
    Comment.objects.create(comment=request.POST['comments'], message=Message.objects.get(id=request.POST['message_id']), user=user_id)
    return redirect('/wall')

def destroy(request):
    print('*'*80)
    dest_id=request.POST['destroyed_id']
    print('destroyed_id is', dest_id)
    destroyed=Message.objects.filter(id=int(dest_id))
    destroyed.delete()
    return redirect('/wall')