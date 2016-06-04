from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from models import *
import random
import string


def main(request):
    # We have 2 types of request GET and POST. GET for page showing and POST for entering in system (cookies storing)
    if request.method == 'POST':  # use POST request for cookies setting up
        try:
            password = request.POST['password']
            login = request.POST['username']

            response = HttpResponseRedirect('/')  # creating response-redirect with cookies
            response.set_cookie('login', login)
            response.set_cookie('password', password)
            return response
        except:
            return HttpResponse('Bad request.')  # using this response when we have an error

    elif request.method == 'GET':
        try:  # cookies checking on login and password presences
            password = request.COOKIES['password']
            login = request.COOKIES['login']
            user = User.objects.get(login=login, password=password)  # checking on user existing
            return render(request, 'button.html')  # render account page with button exit
        except:
            return render(request, 'index.html')  # render main page with login form


def invite_handler(request, invite=''):
    try:  # invite checking
        user = User.objects.get(invite=invite)
    except:
        return HttpResponse('Bad invite')

    if user.password != '':
        return HttpResponse("The invite is invalid.")

    # password generation
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    user.password = password
    user.save()  # writing in DB new User instance

    # Send "email"
    print("Hello, lucky! Your account is active! \n Login: " + user.login + "\nPassword: " + password)
    return HttpResponseRedirect('http://localhost:8000')


# Logouting from accoutn\Deleting cookies
def out(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('login')
    response.delete_cookie('password')
    return response


# Callback which used when invites table is updated
@receiver(post_save, sender=Invites)
def callback(**kwargs):
    invite_users = Invites.objects.exclude(email__in=User.objects.values_list('email'))  # New invites
    for user in invite_users:
        # Generation
        invite = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))
        login = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(10))
        email = user.email
        user = User(invite=invite, login=login, email=email)
        user.save()

        # Send "email"
        print("Hello, lucky! You're getting invite!\n http://localhost:8000/invites/" + invite)
