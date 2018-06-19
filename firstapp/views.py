from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from firstapp.models import Colombina


# Сохраняем данные из формы в бaзу данных
def form_set(request):
    a = request.GET.get('context_value', '')
    a_2 = request.GET.get('title_value', '')
    a_3 = request.GET.get('slug_value', '')
    if str(a) != '' or str(a_2) != '' or str(a_3) != '':
        i = Colombina.objects.create(context=a, title=a_2, slug=a_3)
        i.save()
    return render(request, 'admin1.html')

# Отображение информации из базы данных на главную страницу
def main_page(request):
    y = Colombina.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'main_page.html', context)

# Отображение данных из поля контент
def cnt(request, x):
    y = Colombina.objects.filter(slug=x).values_list()
    template = "template.html"
    context = {
        'context': y[0][1],
        'title': y[0][2]
    }
    return render(request, template, context)
