from django.shortcuts import render


def index(request):
    #incarca anunturi
    return render(request, template_name="base_app/index.html", context={"title": "ChirieShare"})


def conditii(request):
    return render(request, template_name="base_app/termeni_si_conditii.html", context={"title": "Termeni si conditii"})
