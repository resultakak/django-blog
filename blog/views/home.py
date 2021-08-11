from django.shortcuts import render


def home(request):
    context = {
        "title": "Homepage"
    }
    return render(request, 'index.html', context=context)
