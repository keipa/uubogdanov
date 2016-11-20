from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def bootstrap(request):
    return render(request, 'bootstrap.html')


def testing(request):
    return render(request, 'testing.html')


def reviews(request):
    return render(request, 'reviews.html')


class Student():
    def __init__(self, name, graduate_year, rt, ct):
        self.name = name
        self.graduate_year = graduate_year
        self.rt = rt
        self.ct = ct
        self.rise = ct-rt


def central_testing(request):
    people = [
        Student("Яна Поленкова", 2015, 56, 66),
        Student("Костя Жигалев", 2010, 26, 77),
        Student("Вася Пупкин", 2012, 77, 99),
        Student("Фёдор Нагараев", 2010, 74, 76),
        Student("Вячеслав Весёлый", 2011, 16, 66)
    ]
    return render(request, 'central_testing.html', {"people": people})
