from polls.forms import *
from polls.models import *
from django.shortcuts import (render,redirect,get_object_or_404)

# Create your views here.
def index(request, *args, **kwargs):
    template_name = 'index.html'

    persons = Person.objects.all()
    produits = Produit.objects.all()
    magasins = Magasin.objects.all()
    profilMagasin = ProfilMagasin.objects.all()
    # personsMas = Person.objects.filter(sex__gt="feminin")
    # personsFem = Person.objects.filter(sex__gt="masculin")
    context = {'persons':persons,
                'produits':produits,
                'magasins':magasins,
                'profilMagasin':profilMagasin
                # 'personsMas':personsMas,
                # 'personsFem':personsFem
    }
    return render(
        request = request,
        template_name = template_name,
        context = context
    )

def update_person(request, *args, **kwargs):
    template_name = 'update-person.html'
    obj = get_object_or_404(
        Person,
        pk=kwargs.get('pk')
    )   
    if request.method == 'GET':

        print('ok')

        form = PersonForm(
            initial={
                'name':obj.name,
                'age':obj.age,
            }
        )

        print(form)
        context = {
            'form': form
        }
        return render(
            request,
            template_name,
            context
        )
    if request.method == 'POST':
        form = PersonForm(
        request.POST,
        request.FILES,
            initial={
                'name':obj.name,
                'age':obj.name,
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.name = form.cleaned_data.get('sex')
            obj.name = form.cleaned_data.get('age')
            obj.name = form.cleaned_data.get('country')
            obj.save()
            return redirect('home')

        return render(
            request,
            template_name,
            context
        )
