from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'basicapp/index.html')
# Create your views here.


def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            ####DO Something LANGUAGE_CODE
            print("Validataion Success!")
            print("name",form.cleaned_data['name'])
            print("Email",form.cleaned_data['email'])
            print("TEXT",form.cleaned_data['text'])




    return render(request,'basicapp/form_page.html',{'form':form})
