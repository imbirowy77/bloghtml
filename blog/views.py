from django.shortcuts import render


def home(request):
    template = "home.html"
    return render(request, template)

def onas(request):
    template = "onas.html"
    return render(request, template)
def content(request):
    template = "content.html"
    return render(request, template)
def kontakt(request):
    template = "kontakt.html"
    return render(request, template)