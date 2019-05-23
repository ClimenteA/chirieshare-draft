import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import messages
from django.shortcuts import redirect


from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_protect


from .forms import AnunturiForm

from .models import Mesaje, Colegi


@login_required
def adauga(request):

    if request.method == "POST":
        form = AnunturiForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            messages.success(request, 'Anuntul tau a fost adaugat!')
            return redirect("/")
        else:
            messages.error(request, 'Datele trimise nu sunt valide!')
            return redirect("/")
    else:
        form = AnunturiForm()

    context = {
        "title": "Adauga anunt",
        "form": form
        }
    return render(request, template_name='anunturi/adauga_anunt.html', context=context)




@login_required
def mesaj(request):

    if request.is_ajax():
        if request.method == "POST":
            print(request.body)


    # if request.method == "POST":
    #     form = MesajeForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.anunt = form.cleaned_data["anunt"]
    #         form.save()
    #         messages.success(request, 'Mesajul tau a fost trimis!')
    #         return redirect("/")
    #     else:
    #         messages.error(request, 'Datele trimise nu sunt valide!')
    #         return redirect("/")
    # else:
    #     form = MesajeForm()

    # context = {
    #     "title": "Adauga",
    #     "form": form
    #     }

    # return render(request, template_name='anunturi/anunt.html', context=context)








@login_required
def colegi(request):
    pass