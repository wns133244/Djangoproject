from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.utils import timezone

from app.models import Member, LoginForm


def index(request):
        template = loader.get_template('app/index.html')
        context = {
            'latest_question_list': "test",
        }
        return HttpResponse(template.render(context, request))

def index2(request):
        template2 = loader.get_template('app/index2.html')
        context2 = {
            'latest_question_list': "test",
        }
        return HttpResponse(template2.render(context2, request))


def sign(request):
    template2 = loader.get_template('app/sign.html')
    context2 = {
        'latest_question_list': "test",
    }
    return HttpResponse(template2.render(context2, request))

def join(request):
     if request.method == 'GET':
         return render(request, 'app/join.html', {})
     else:
         user_name = request.POST['user_name']
         user_mail = request.POST['user_mail']
         user_birth = request.POST['user_birth']

         member = Member(user_name=user_name, user_mail=user_mail, user_birth=user_birth)
         member.c_date = timezone.now()
         member.save()
     return HttpResponse('로그인 완료' + user_name + user_mail + user_birth)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'app/login.html', {'form': form})
    else:
        user_name = request.POST['user_name']
        user_mail = request.POST['user_mail']

        try:
            Member.objects.get(user_name=user_name, user_mail=user_mail)
        except Member.DoesNotExist:
            return HttpResponse('로그인 성공')
        else:
            return HttpResponse('로그인 실패')

def index3(request):
        template3 = loader.get_template('app/index3.html')
        context3 = {
            'latest_question_list': "test",
        }
        return HttpResponse(template3.render(context3, request))


def card(request):
    template4 = loader.get_template('app/card.html')
    context4 = {
        'latest_question_list': "test",
    }
    return HttpResponse(template4.render(context4, request))

def card2(request):
    template4 = loader.get_template('app/card2.html')
    context4 = {
        'latest_question_list': "test",
    }
    return HttpResponse(template4.render(context4, request))
