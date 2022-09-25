from django.shortcuts import render


def just_the_temp(request):
    return render(request, 'just_the_temp.html')