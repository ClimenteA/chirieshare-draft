from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from anunturi.models import Anunturi
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
    utilizator = get_object_or_404(User, pk=anunt.user_id)
    context = {
        "title": "Anunt", 
        'anunt': anunt, 
        'utilizator': utilizator
    }

    return render(request, template_name="anunturi/anunt.html", context=context)



def conditii(request):
    return render(request, template_name="base_app/termeni_si_conditii.html", context={"title": "Termeni si conditii"})
