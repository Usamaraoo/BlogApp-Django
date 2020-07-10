from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        ContactForm()
    context = {'form': form}
    return render(request, 'form.html', context)
