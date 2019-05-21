from django.shortcuts import render
from anunturi.models import Anunturi

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def anunt(request):
    
    return render(request, "base_app/index.html", context={"title": "Anunt"})




def conditii(request):
    return render(request, template_name="base_app/termeni_si_conditii.html", context={"title": "Termeni si conditii"})
