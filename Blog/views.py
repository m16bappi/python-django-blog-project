from django.shortcuts import render

data = [
    {
        "name": "Mehedi",
        "age": 23
    },
    {
        "name": "Munna",
        "age": 25
    },
    {
        "name": "Shamim",
        "age": 22
    },
    {
        "name": "Ador",
        "age": 26
    }
]


def Home(request):
    return render(request, "Home.html", {"data": data})


def About(request):
    return render(request, "About.html", {})
