from django.shortcuts import render


def contact(request):
    context = {
        "title": "Contact"
    }
    return render(request, 'pages/contact.html', context=context)
