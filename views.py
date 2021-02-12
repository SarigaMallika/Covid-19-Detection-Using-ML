from django.shortcuts import render
from django.contrib.sessions.models import Session
from .models import user_details
from .models import medical_details
from .models import symp
from .models import message
from .models import admin

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def user_reg(request):
    return render(request,'user_reg.html')
def save_user(request):
    try:
        alreadyuser = user_details.objects.get(username = request.POST.get('uname'))
    except:
        alreadyuser= None
    if alreadyuser==None:
        db = user_details(name=request.POST.get('fname'),dob=request.POST.get('dob'),place=request.POST.get('place'),phone=request.POST.get('phone'),email=request.POST.get('email'),username=request.POST.get('uname'),password=request.POST.get('password'))
        db.save()
        return render(request, 'user_reg.html', {'msg': "Successfully Inserted"})
    else:
        return render(request, 'user_reg.html', {'msg': "Username Already Taken"})
def med_reg(request):
    return render(request,'med_reg.html')

def save_medical(request):
    db = medical_details(name=request.POST.get('fname'), dob=request.POST.get('dob'), place=request.POST.get('place'),
                      phone=request.POST.get('phone'), email=request.POST.get('email'),gender=request.POST.get('gender'),
                      username=request.POST.get('uname'), password=request.POST.get('password'))
    db.save()
    return render(request, 'med_reg.html', {'msg': "Successfully Inserted"})

def user_login(request):
    return render(request,'user_login.html')
def medical_login(request):
    return render(request,'medical_login.html')
def admin_login(request):
    return render(request,'admin_login.html')
def user_log(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    ad = user_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['user'] = x.username

            return render(request, 'user_home.html', {'user': x.username})
    return render(request, 'user_login.html', {'msg': "Incorrect username or password.Try again"})


def user_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['user'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'user_login.html')


def add_symptoms(request):
    user = request.session['user']
    u_id = user_details.objects.get(username = user)
    return render(request,'add_symptoms.html',{'user':user,'u_id':u_id})

def save_symptoms(request):
   import numpy as np
   import pandas as pd
   from sklearn.model_selection import train_test_split
   from sklearn.naive_bayes import GaussianNB
   from sklearn.metrics import accuracy_score
   import matplotlib.pyplot as plt
   import seaborn as sns

   df = pd.read_csv('C:/Users/LENOVO/source/repos/FathimaPython/static/sample_dataset.csv')

   x = df.drop('Result', axis=1)
   y = df['Result']

   x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.003, random_state=42)

   model = GaussianNB()
   model.fit(x_train, y_train)

   y_pred = model.predict(x_test)
   print(y_pred)

   data = {'id': [10000], 'Age':request.POST.get('age'), 'Fever':request.POST.get('fever'), 'Fatigue':request.POST.get('fatigue'), 'Dry cough':request.POST.get('cough'), 'Loss of appetite':request.POST.get('loss_of_appetite'),
            'Body aches':request.POST.get('body_aches'), 'Shortness of breath':request.POST.get('shortness_of_breath'), 'Mucus':request.POST.get('mucus'), 'Sore throat':request.POST.get('sore_throat'), 'Headache':request.POST.get('headache'),
            'Chills':request.POST.get('chills'), 'Loss of smell':request.POST.get('loss_of_smell'), 'Stuffy nose':request.POST.get('stuffy_nose'), 'Vomiting':request.POST.get('vomiting'), 'Diarrhea':request.POST.get('diarrhea'),
            'Trouble breathing':request.POST.get('trouble_breathing'), 'Constant pain':request.POST.get('constant_pain'), 'Bluish lips':request.POST.get('bluish_lips'), 'Sudden confusion':request.POST.get('sudden_confusion')}
   df = pd.DataFrame(data)
   actual_predict = model.predict(df)
   actual_predict = actual_predict[0]

   print(actual_predict)
   user = request.session['user']
   db = symp(age=request.POST.get('age'),fever=request.POST.get('fever'),fatigue=request.POST.get('fatigue'),dry_cough=request.POST.get('cough'),loss_of_appetite=request.POST.get('loss_of_appetite'),body_aches=request.POST.get('body_aches'),shortness_of_breath=request.POST.get('shortness_of_breath'),mucus=request.POST.get('mucus'),sore_throat=request.POST.get('sore_throat'),headache=request.POST.get('headache'),chills=request.POST.get('chills'),loss_of_smell=request.POST.get('loss_of_smell'),stuffy_nose=request.POST.get('stuffy_nose'),vomiting=request.POST.get('vomiting'),diarrhea=request.POST.get('diarrhea'),trouble_breathing=request.POST.get('trouble_breathing'),constant_pain=request.POST.get('constant_pain'),bluish_lips=request.POST.get('bluish_lips'),sudden_confusion=request.POST.get('sudden_confusion'),u_id=request.POST.get('u_id'),result=actual_predict)
   db.save()
   return render(request, 'add_symptoms.html', {'msg': "Successfully Inserted",'user':user})


def medical_log(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    ad = medical_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['medical'] = x.username

            return render(request, 'medical_home.html', {'medical': x.username})
    return render(request, 'medical_login.html', {'msg': "Incorrect username or password.Try again"})


def med_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['medical'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'medical_login.html')


def view_users(request):
    medical = request.session['medical']
    user = user_details.objects.all()
    return render(request, 'view_users.html', {'medical': medical,'user':user})

def view_symptoms(request):
    medical = request.session['medical']
    sym = symp.objects.all()
    return render(request, 'view_symptoms.html', {'medical': medical, 'sym': sym})

def send_message(request):
    medical = request.session['medical']
    return render(request,'message.html',{'medical': medical})

def save_message(request):
    medical = request.session['medical']
    db = message(u_id=request.POST.get('u_id'), message=request.POST.get('message'))
    db.save()
    return render(request, 'message.html', {'msg': "Successfully Send",'medical': medical})

def view_reply(request):
    user = request.session['user']
    #print(user)
    user_id = user_details.objects.get(username=user)
    #print(user_id.id)
    try:
      reply = message.objects.get(u_id = user_id.id)
      return render(request, 'view_reply.html', {'user': user, 'reply': reply})
    except:
        return render(request, 'view_reply.html', {'user': user})


def admin_log(request):
    username = request.POST.get('uname')
    #print(username)
    password = request.POST.get('password')
    admin_values = admin.objects.all()
    for x in admin_values:
       if x.username == username and x.password == password:
            request.session['admin'] = x.username
            return render(request, 'admin_home.html', {'admin': x.username})
    return render(request, 'admin_login.html', {'msg': "Incorrect username or password.Try again"})


def admin_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['admin'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'admin_login.html')

def all_users(request):
    admin = request.session['admin']
    user = user_details.objects.all()
    return render(request, 'all_users.html', {'admin': admin,'user':user})

def all_medicals(request):
    admin = request.session['admin']
    medical = medical_details.objects.all()
    return render(request, 'all_medicals.html', {'admin': admin,'medical':medical})

def all_result(request):
    admin = request.session['admin']
    sym = symp.objects.all()
    return render(request, 'all_result.html', {'admin': admin, 'sym': sym})

def all_reply(request):
    admin = request.session['admin']
    reply = message.objects.all()
    return render(request, 'all_reply.html', {'admin': admin, 'reply': reply})
