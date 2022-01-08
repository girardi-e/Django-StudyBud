from django.shortcuts import render

rooms = [
    {'id': 1, "name": "Let's learn Python!"},
    {'id': 2, "name": "Design with me"},
    {'id': 3, "name": "Front-end Developers"},
]


def home(request):
    return render(request, "home.html", {"rooms": rooms})


def room(request):
    return render(request, 'room.html')
