from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Patient ,Avis ,Video

from datetime import datetime, time as datetime_time
# Create your views here.
def interface(request):
    return render(request,'interface.html')

def login(request):
    return render(request, 'Login.html')
def filter(request):
    if request.method == "POST":
        date_str = request.POST.get('filter_date')

        try:
            patients = Patient.objects.filter(date=date_str)

            context = {"data": patients, "filter_date": date_str}
            return render(request, 'filter.html', context)

        except Patient.DoesNotExist:
            messages.error(request, 'Aucun patient trouvé pour la date spécifiée.')
            return redirect("page2")

    return redirect("page2")

def about(request):
    video=Video.objects.all()
    context={"video":video}
    return render(request, 'about.html',context)

def avis(request):
    avis=Avis.objects.all()
    context={"avis":avis}
    return render(request, 'avis.html',context)

def ajoutAvis(request):
    if request.method == "POST":
        prod=Avis()
        prod.firstName=request.POST.get('nom')
        prod.lastName=request.POST.get('prenom')
        prod.avis=request.POST.get('avis')
        if len(request.FILES)!=0:
            prod.image=request.FILES['image']
        prod.save()
        return redirect('avis')
    return render(request, 'ajoutAvis.html')

def SignIn(request):
    return render(request, 'SignIn.html')

def page2(request):
    data=Patient.objects.all()
    context={"data":data}
    return render(request, 'page2.html',context)
def insert(request):
    if request.method=="POST":
        current_date = datetime.now().date()
        user_time_str = request.POST.get('time')
        user_date_str = request.POST.get('date')
        user_time = datetime.strptime(user_time_str, '%H:%M').time()
        user_date = datetime.strptime(user_date_str, '%d/%m/%Y').date()
        if user_date < current_date:
            messages.error(request, 'La date ne peut pas être inférieure à la date courante.')
            return redirect("SignIn")
        if not (datetime_time(9, 0) <= user_time <= datetime_time(13, 0)):
            messages.error(request, 'L\'heure doit être comprise entre 9h et 13h.')
            return redirect("SignIn")
        
        firstName=request.POST.get('nom')
        lastName=request.POST.get('prenom')
        email=request.POST.get('email')
        gender=request.POST.get('sexe')
        age=request.POST.get('age')
        city=request.POST.get('ville')
        phone=request.POST.get('phone')
        allergies=request.POST.get('allergies')
        medications=request.POST.get('medications')
        date=request.POST.get('date')
        time=request.POST.get('time')
        query=Patient(firstName=firstName,lastName=lastName,email=email,gender=gender,age=age,city=city,phone=phone,allergies=allergies,medications=medications,date=date,time=time)
        query.save()
        print(firstName,lastName,gender,date,allergies)
        return redirect("page2")   
    return render(request, 'page2.html')

def update(request,id):
    if request.method=="POST":
        firstName=request.POST['nom']
        lastName=request.POST['prenom']
        email=request.POST['email']
        gender=request.POST['sexe']
        age=request.POST['age']
        city=request.POST['ville']
        phone=request.POST['phone']
        allergies=request.POST['allergies']
        medications=request.POST['medications']
        date=request.POST['date']
        time=request.POST['time']

        edit=Patient.objects.get(id=id)
        edit.firstName=firstName
        edit.lastName=lastName
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.city=city
        edit.phone=phone
        edit.allergies=allergies
        edit.medications=medications
        edit.date=date
        edit.time=time
        edit.save()
        return redirect("page2")
    d=Patient.objects.get(id=id)
    context={"d":d}
    return render(request, 'update.html',context)

def delete(request,id):
    d=Patient.objects.get(id=id)
    d.delete()
    return redirect("page2")