from os import link
from django.shortcuts import redirect, render, get_object_or_404
from links.models import Link
from links.forms import LinkForm

def index(request):
    links = Link.objects.all()
    return render(request,'index.html',{
        'links' : links
    })
def create(request):
    form = LinkForm(request.POST or None)
    if form.is_valid():
        link = form.save()
        return redirect("show",pk=link.pk)
    return render(request,'create.html',{'form' : form,})



def show(request, pk):
    link = get_object_or_404(Link, pk=pk)
    return render(request,'show.html',{'link':link})

def update(request, pk):
    link = get_object_or_404(Link , pk=pk)
    form = LinkForm(request.POST or None, instance=link)
    if form.is_valid():
        link = form.save()
        return redirect('show',pk=link.pk)

    return render(request,'update.html',{'form':form})

def delete(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('index')

def go(request, code):
    link = get_object_or_404(Link, code=code)
    return redirect(link.url)