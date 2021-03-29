from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('About page')


def home(request):
    return render(request, 'home_page.html')


def reverse(request):
    input_user = request.GET['input']
    words = input_user.split()
    number_of_words = len(words)
    reversed_input = input_user[::-1]
    return render(request, 'reverse.html', {'input': input_user,
                                            'reversed_input': reversed_input,
                                            'number_of_words': number_of_words})
