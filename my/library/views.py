from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template import loader
from pathlib import Path
from django import forms
import os
from . import util


class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control"}))

def search(request, ask):
    res = []
    books = util.list_books()
    for i in books:
        if i.lower() == ask.lower():
            res.append(i)
            return render(request, "search_results.html", {
                "books": res,
                "form": SearchForm()
            })
    for i in books:
        if ask.lower() in i.lower():
            res.append(i)
    if len(res) > 0:
        return render(request, "search_results.html", {
            "books": res,
            "form": SearchForm()
        })
    else:
        return render(request, "no_results.html", {
            "form": SearchForm()
        })

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            "form": SearchForm()
        })
    return render(request, 'upload.html',{
        "form": SearchForm()
    })


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            ask = form.cleaned_data['search']
            return search(request, ask)
            return HttpResponse(ask)
    else:
        return render(request, "index.html", {
            "books": util.list_books(),
            "form": SearchForm()
        })
