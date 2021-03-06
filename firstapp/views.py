from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.forms.models import model_to_dict

# Create your views here.
from firstapp.models import Colombina


# Сохраняем данные из формы в бaзу данных
def addArticles(request):
    a = request.GET.get('context_value', '')
    a_2 = request.GET.get('title_value', '')
    a_3 = request.GET.get('slug_value', '')
    if str(a) != '' or str(a_2) != '' or str(a_3) != '':
        i = Colombina.objects.create(context=a, title=a_2, slug=a_3)
        i.save()
    return render(request, 'admin/addArticles.html')


# Редактируем данные из базы
def editArticles(request, x):
    y = Colombina.objects.get(id=x)
    print(y)
    if request.method == 'POST':
        y.title = request.POST.get('title_value', '')
        y.slug = request.POST.get('slug_value', '')
        y.context = request.POST.get('context_value', '')
        y.save()
        # a = request.GET.get('context_value', '')
        # a_2 = request.GET.get('title_value', '')
        # a_3 = request.GET.get('slug_value', '')
        # a_0 = request.GET.get('id_value', '')
        # print(a, a_2, a_3, a_0)
        # # if str(a) != '' or str(a_2) != '' or str(a_3) != '':
        # Colombina.objects.filter(id=a_0).update(context=a, title=a_2, slug=a_3)
        return render(request, 'admin/articles.html')
    else:
        context = {
             'id': y.id,
             'context': y.context,
             'title': y.title,
             'slug': y.slug
        }
        print(context)
        return render(request, 'admin/editArticles.html', context)

# Удаляем данные из базы
def delArticles(request, x):
    y = Colombina.objects.get(id=x)
    print(y)
    if request.method == 'POST':
        y.delete()
        return render(request, 'admin/articles.html')
    else:
        context = {
             'id': y.id,
             'context': y.context,
             'title': y.title,
             'slug': y.slug
        }
        print(context)
        return render(request, 'admin/delArticles.html', context)


# Отображение информации из базы данных на главную страницу
def articles(request):
    y = Colombina.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'admin/articles.html', context)


# Отображение данных из поля контент
def cnt(request, x):
    z = Colombina.objects.filter(slug=x).values_list()
    print(z)
    template = "user/template.html"
    context = {
        'context': z[0][1],
        'title': z[0][2]
    }
    return render(request, template, context)


# Отображение данных из поля title
def title(request):
    y = Colombina.objects.values_list().values()
#    y = Colombina.objects.values_list().values()
#    template = "user/template.html"
#    context = model_to_dict(y)
#    context = [entry for entry in y]
    context = {
        'context_value': y,
     }
#    return render(request, template, context)
    return render(request, 'user/main.html', context)


# Отображение данных из поля title
def adminka(request):
    return render(request, 'admin/admin.html')

