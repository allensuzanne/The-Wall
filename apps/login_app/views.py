from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
from django.http import JsonResponse

def index(request):
    if 'user' in request.session:    
        del request.session['user']
    found = False
    context = {
        'users': User.objects.all()
    }
    #if request.method=='POST':
        #reuser = User.objects.filter(email=request.POST['email'])
    #if reuser:
    #    found=True
    #return render(request, 'login_app/partials/email.html', found)
    return render(request, "login_app/index.html", context)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.get(email__iexact=email).exists()
    }
    return JsonResponse(data)

def validate(request):
    errors = User.objects.basic_validator(request.POST)
    reuser = User.objects.filter(email=request.POST['email'])
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password=request.POST['password']
        pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash.decode())
        print('*'*80)
        print(password, pw_hash)
        request.session['user']=request.POST['first_name']
        request.session['user_id']=new_user.id
        return redirect ('/wall')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user=User.objects.filter(email=request.POST['email'])
        logged_user=user[0]
        request.session['user'] = logged_user.first_name
        request.session['user_id']=logged_user.id
        return redirect ('/wall')

def success(request):
    if 'user' in request.session:
        return render(request, "login_app/success.html")
    else:
        return redirect ('/')