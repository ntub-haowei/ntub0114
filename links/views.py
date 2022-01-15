from django.shortcuts import redirect, render
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
        form.save()
        return redirect("/")
    return render(request,'create.html',{
        'form' : form,
    })