import itertools

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

from anunturi.models import Anunturi, Share
from users.models import User



def index(request):
    anunturi_publicate = Anunturi.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(anunturi_publicate, 5)

    try:
        anunturi_pub = paginator.page(page)
    except PageNotAnInteger:
        anunturi_pub = paginator.page(1)
    except EmptyPage:
        anunturi_pub = paginator.page(paginator.num_pages)

    return render(request, template_name="base_app/index.html", context={"title": "ChirieShare", "anunturi": anunturi_pub})


def anunt(request, id_anunt):
    anunt = get_object_or_404(Anunturi, pk=id_anunt)
    postat_de = get_object_or_404(User, pk=anunt.user_id)

    # Share.objects.filter() must filter user id by curent anunt not to get all users from share table

    colegideshare_ids = list(set(itertools.chain(*Share.objects.values_list("user_id"))))

    colegideshare = []
    for cid in colegideshare_ids:
        u = User.objects.get(pk=cid)
        u_data = {
            'first_name': u.first_name,
            'email': u.email,
            'imagine': u.imagine,
            'ocupatie': u.ocupatie,
            'varsta': u.varsta,
            'sex': u.sex
        }

        colegideshare.append(u_data)

    context = {
        "title": "Anunt", 
        'anunt': anunt, 
        'postat_de': postat_de,
        'lashare': Share.objects.filter(user_id=request.user.id).exists(),
        'colegideshare': colegideshare
    }

    return render(request, template_name="anunturi/anunt.html", context=context)



def conditii(request):
    return render(request, template_name="base_app/termeni_si_conditii.html", context={"title": "Termeni si conditii"})
