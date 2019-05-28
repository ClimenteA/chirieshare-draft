import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import messages
from django.shortcuts import redirect


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Anunturi
from .forms import AnunturiForm

from .models import Proprietar, Chirias, Share


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


def sheriasi(request):
    return ""






# #TODO SECURITY CSRF HERE MAKE IT A POST AJAX REQUEST!
# # But since the user must be logged in.. I think a GET request will be good for now
# @csrf_exempt
# @login_required
# def chirias(request):

#     msg = Chirias()
#     msg.anunt_id = int(request.GET["id_anunt"])
#     msg.user_id = request.user.id
#     msg.mesaj = request.GET["mesaj"] 
#     msg.save()

#     return JsonResponse({'status': 200})


# @csrf_exempt
# @login_required
# def share(request):

#     sh = Share()
#     sh.anunt_id = int(request.GET["id_anunt"])
#     sh.user_id = request.user.id
#     sh.save()

#     return JsonResponse({'status': 200})



