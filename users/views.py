from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import UserForm, UserUpdateForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#For testing
from django.http import HttpResponse


def autentificare(request):
    context = {
        "title": "Intra/Creeaza cont",
        "form": UserForm()
    }
    return render(request, "users/autentificare.html", context=context) 


def logare(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            utilizator = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if utilizator is not None:
                login(request, utilizator)
                messages.success(request, 'Spor la navigat!')
                return redirect("/")
            else:
                messages.error(request, 'Emailul introdus nu este in baza de date!')
                return redirect("/")
        else:
            messages.error(request, 'Datele trimise nu sunt valide!')
            return redirect("/")
    else:
        form = UserForm() #send an empty form
        
    return render(request, template_name="users/autentificare.html", context={"form": form}) 


def inregistrare(request):

    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid() and len(form.cleaned_data['password']) >= 8:
            
            if not User.objects.filter(email=form.cleaned_data['email']).exists():
                User.objects.create_user(
                    username=form.cleaned_data['email'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                messages.success(request, 'Acum poti sa te loghezi in contul tau!')
                return redirect("/")
            else:
                messages.error(request, 'Emailul exista in baza de date!')
                return redirect("/")
        else:
            messages.error(request, 'Datele trimise nu sunt valide!')
            return redirect("/") 
    else:
        form = UserForm() #send an empty form

    return render(request, template_name="users/autentificare.html", context={"form": form}) 



def delogare(request):
    logout(request)
    messages.success(request, 'Te-ai delogat!')
    return redirect("/")




def resetare(request):
    if request.method == "POST":
        pass



def utilizator(request, id_user=None, id_anunt=None):

    if id_user:
        utilizator = get_object_or_404(User, pk=id_user)
    else:
        utilizator = None

    context = {"title": "Utilizator", "utilizator_share": utilizator, "id_anunt": id_anunt}
    
    return render(request, template_name="users/utilizator.html", context=context) 
    


@login_required
def message(request, id_user, id_anunt):
    
    context = {"title": "Mesaje"}
    
    return render(request, template_name="users/messaging.html", context=context) 





@login_required
def actualizare(request):
    
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            u = User.objects.get(username=request.user.username)
            u.first_name = form.cleaned_data['first_name'] if len(str(form.cleaned_data['first_name'])) > 3 else u.first_name 
            u.sex = form.cleaned_data['sex'] if form.cleaned_data['sex'] != "N" else u.sex 
            u.ocupatie = form.cleaned_data['ocupatie'] if len(str(form.cleaned_data['ocupatie'])) >= 4 else u.ocupatie 
            u.varsta = form.cleaned_data['varsta'] if form.cleaned_data['varsta'] != None else u.varsta 
            u.telefon = form.cleaned_data['telefon'] if len(str(form.cleaned_data['telefon'])) >= 10 else u.telefon 
            try:
                u.imagine = request.FILES["imagine"] #FILES["name of attr"]
            except:
                pass
            
            u.save()

            messages.success(request, 'Datele trimise au fost salvate!')
            return redirect("/")
        else:
            messages.success(request, 'Datele trimise nu sunt valide!')
            return redirect("/")
    else:
        form = UserUpdateForm()
        
    
    context = {
        "form": form,
        "title": "Actualizare cont",
    }
    
    return render(request, template_name="users/modificare_utilizator.html", context=context) 




