from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from firstapp.models import Colombina


# Сохраняем данные из формы в бозу данных
def form_set(request):
    a = request.GET.get('context_value', '')
    if str(a) != '':
        i = Colombina.objects.create(context=a)
        i.save()
    return render(request, 'admin1.html')


# Отображение информации из базы данных на главную страницу
def main_page(request):
    y = Colombina.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'main_page.html', context)
