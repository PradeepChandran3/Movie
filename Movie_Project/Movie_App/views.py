from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import  Movie
from . forms import MovieForm

# Create your views here.
def index (request):
    movie=Movie.objects.all()
    context={
        'movie_list': movie
    }
    return render(request,"index.html", context)
def detail (request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render (request,"details.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('Name')
        desc = request.POST.get('Description')
        year = request.POST.get('Year')
        img = request.FILES['Image']
        movie=Movie(Name=name,Description=desc,Year=year,Image=img)
        movie.save()
    return render(request,'add.html')

def Update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm (request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render(request,"edit.html",{'form':form,'movie':movie})

def Delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

