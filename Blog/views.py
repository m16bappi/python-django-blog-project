from django.shortcuts import render


def Home(request):
    return render(request, "Home.html", {})

def About(request):
    return render(request, "About.html", {})
