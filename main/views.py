from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app': 'Raja inventory',
        'name': 'Pak Bepe',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)