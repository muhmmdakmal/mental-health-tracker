from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245125',
        'name': 'Muhammad Akmal Abdul Halim',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)