from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


class Review:
    def __init__(self, title, name, content):
        self.title = title
        self.name = name
        self.content = content


class Student:
    def __init__(self, name, graduate_year, rt, ct):
        self.name = name
        self.graduate_year = graduate_year
        self.rt = rt
        self.ct = ct
        self.rise = ct-rt


def index(request):
    r = [
        Review("This is the first slide",
               "A short description of the contents of this slide",
               "<p>Collaboratively administrate empowered markets via plug-and-play networks. Dynamically procrastinate B2C users after installed base benefits. Dramatically visualize customer directedconvergence without revolutionary ROI.</p><p>Efficiently unleash cross-media information without cross-media value. Quickly maximize timelydeliverables for real-time schemas. Dramatically maintain clicks-and-mortar solutions withoutfunctional solutions.</p><p>Completely synergize resource taxing relationships via premier niche markets. Professionallycultivate one-to-one customer service with robust ideas. Dynamically innovate resource-levelingcustomer service for state of the art customer service.</p>"),
        Review("This is the first slide",
               "A short description of the contents of this slide",
               "<p>Collaboratively administrate empowered markets via plug-and-play networks. Dynamically procrastinate B2C users after installed base benefits. Dramatically visualize customer directedconvergence without revolutionary ROI.</p><p>Efficiently unleash cross-media information without cross-media value. Quickly maximize timelydeliverables for real-time schemas. Dramatically maintain clicks-and-mortar solutions withoutfunctional solutions.</p><p>Completely synergize resource taxing relationships via premier niche markets. Professionallycultivate one-to-one customer service with robust ideas. Dynamically innovate resource-levelingcustomer service for state of the art customer service.</p>"),
        Review("This is the first slide",
               "A short description of the contents of this slide",
               "<p>Collaboratively administrate empowered markets via plug-and-play networks. Dynamically procrastinate B2C users after installed base benefits. Dramatically visualize customer directedconvergence without revolutionary ROI.</p><p>Efficiently unleash cross-media information without cross-media value. Quickly maximize timelydeliverables for real-time schemas. Dramatically maintain clicks-and-mortar solutions withoutfunctional solutions.</p><p>Completely synergize resource taxing relationships via premier niche markets. Professionallycultivate one-to-one customer service with robust ideas. Dynamically innovate resource-levelingcustomer service for state of the art customer service.</p>")
    ]
    return render(request, 'index.html', {"reviews": r})


def bootstrap(request):
    return render(request, 'bootstrap.html')


def testing(request):
    return render(request, 'testing.html')


def reviews(request):
    return render(request, 'reviews.html')



def central_testing(request):
    people = [
        Student("Яна Поленкова", 2015, 56, 66),
        Student("Костя Жигалев", 2010, 26, 77),
        Student("Вася Пупкин", 2012, 77, 99),
        Student("Фёдор Нагараев", 2010, 74, 76),
        Student("Вячеслав Весёлый", 2011, 16, 66)
    ]
    return render(request, 'central_testing.html', {"people": people})
