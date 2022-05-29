from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):

    context = {'pagename': 'Просмотр сниппетов',
               'snippets': Snippet.objects.all(),
               }
    return render(request, 'pages/view_snippets.html', context)

def single_snippet_page(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        context = {
            'pagename': 'Страница сниппета',
            'snippet': snippet,
            }

        return render(request, 'pages/snippet_page.html', context)

    except ObjectDoesNotExist:
        raise Http404



