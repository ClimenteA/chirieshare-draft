import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import messages
from django.shortcuts import redirect


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from users.models import User

from .models import Anunturi, Mesaje, Sheriasi
from .forms import AnunturiForm


@login_required
def adauga(request):
    """
        Reda pagina anunt sau salveaza datele trimise
    """
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



def sheriasi(request, id_anunt):
    """
        Populate 'Colegi de share' section with people who joined the current listing
    """

    colegideshare_ids = Sheriasi.objects.filter(anunt_id=id_anunt).values_list('user_id', flat=True)
    current_user_added = True if request.user.id in colegideshare_ids else False

    colegideshare = []
    for cid in colegideshare_ids:
        u = User.objects.get(pk=cid)
        u_data = {
            'id': u.id,
            'first_name': u.first_name,
            'email': u.email,
            'imagine': u.imagine if u.imagine else "",
            'ocupatie': u.ocupatie,
            'varsta': u.varsta,
            'sex': u.sex
        }

        colegideshare.append(u_data)

    status = 200 if len(colegideshare) > 0 else 204

    
    data = {'status': status, 'colegideshare': colegideshare, 'current_user_added': current_user_added}
    
    return JsonResponse(data)



@login_required
def join_sheriasi(request, id_anunt):
    """
        Add current user to Sheriasi table
        Send message to all (if any) users joined to this listing 
    """
    
    Sheriasi.objects.create(anunt_id=id_anunt, user_id=request.user.id).save()
    #Send messages to all sheriasi 
    users = Sheriasi.objects.filter(anunt_id=1).values_list('user_id', flat=True)
    users = [u for u in users if not u == request.user.id]
    
    for destinatar in users:
        Mesaje.objects.create(
            mesaj="Sunt interesat sa impart chiria pentru acest imobil!",
            anunt_id=id_anunt,
            destinatar_id=destinatar,
            expeditor_id=request.user.id
        ).save()

    # print("join", users)

    return redirect('sheriasi', id_anunt=id_anunt)

    


@login_required
def remove_sheriasi(request, id_anunt):
    """
        Remove current user from Sheriasi table
        Send message to all (if any) users joined to this listing 
    """
    
    Sheriasi.objects.filter(anunt_id=id_anunt, user_id=request.user.id).delete()
    #Send messages to all sheriasi 
    users = Sheriasi.objects.filter(anunt_id=1).values_list('user_id', flat=True)
    users = [u for u in users if not u == request.user.id]

    for destinatar in users:
        Mesaje.objects.create(
            mesaj="Nu mai sunt interesat sa impart chiria pentru acest imobil!",
            anunt_id=id_anunt,
            destinatar_id=destinatar,
            expeditor_id=request.user.id
        ).save()

    # print("remove", users)

    return redirect('sheriasi', id_anunt=id_anunt)





@login_required
def chirias(request):

    msg = Chirias()
    msg.anunt_id = int(request.GET["id_anunt"])
    msg.user_id = request.user.id
    msg.mesaj = request.GET["mesaj"] 
    msg.save()

    return JsonResponse({'status': 200})


# @csrf_exempt
# @login_required
# def share(request):

#     sh = Share()
#     sh.anunt_id = int(request.GET["id_anunt"])
#     sh.user_id = request.user.id
#     sh.save()

#     return JsonResponse({'status': 200})



