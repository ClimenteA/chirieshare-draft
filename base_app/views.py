from django.shortcuts import render
from anunturi.models import Anunturi


def index(request):

    # anunturi_publicate = Anunturi.objects.all()

    return render(request, template_name="base_app/index.html", context={"title": "ChirieShare"})


def conditii(request):
    return render(request, template_name="base_app/termeni_si_conditii.html", context={"title": "Termeni si conditii"})
