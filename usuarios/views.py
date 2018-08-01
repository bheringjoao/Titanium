from django.shortcuts import render
from usuarios.forms import UserModelForm, CharacterModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Character, Event, Slot, Vocation, World
import math

# Create your views here.

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'usuarios/cadastro.html', context)

def do_login(request):
    if request.user.id is not None:
        return redirect('/perfil')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/perfil')
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, 'usuarios/login.html')

def do_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def perfil(request):
    context = {'chars': Character.objects.filter(user_id=request.user.id)}
    return render(request, 'usuarios/perfil.html', context)

@login_required
def create_character(request):
    form = CharacterModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            addChar = Character()
            addChar.name = form.cleaned_data['name']
            addChar.level = form.cleaned_data['level']
            addChar.vocation = form.cleaned_data['vocation']
            addChar.world = form.cleaned_data['world']
            addChar.user = request.user
            addChar.save()
            messages.success(request, "Personagem criado com sucesso!")
            return redirect('/perfil')
    return render(request, 'usuarios/personagem.html', context)

@login_required
def update_character(request, id):
    character = Character.objects.get(id=id)
    form = CharacterModelForm(request.POST or None, instance=character)
    context = {'form': form, 'character': character, 'page_title': "Editar"}

    if request.method == 'POST':
        if form.is_valid():
            if character.user.id == request.user.id:
                form.save()
                messages.success(request, "Personagem salvo com sucesso!")
                return redirect('/perfil')
            else:
                messages.error(request, "Você não tem permissão para realizar esta ação.")
    return render(request, 'usuarios/personagem.html', context)

@login_required
def delete_character(request, id):
    character = Character.objects.get(id=id)
    form = CharacterModelForm(request.POST or None, instance=character)
    context = {'form': form, 'character': character, 'page_title': "Excluir"}

    if request.method == 'POST':
        if character.user.id == request.user.id:
            character.delete()
            messages.success(request, "Personagem excluído com sucesso!")
            return redirect('/perfil')
        else:
            messages.error(request, "Você não tem permissão para realizar esta ação.")
    return render(request, 'usuarios/personagem.html', context)

@login_required
def search_event(request, id):
    if id == 0:
        events = Event.objects.all()
        for e in events:
            e.slots = Slot.objects.filter(event_id=e.id)
    else:
        events = Event.objects.filter(slot__character_id=id)
        for e in events:
            e.slots = Slot.objects.filter(event_id=e.id)

    context = {'events': events}
    return render(request, 'usuarios/eventos.html', context)

@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)
    event.slots = Slot.objects.filter(event_id=event.id)

    context = {'event': event, 'chars': Character.objects.filter(user_id=request.user.id)}

    if request.method == 'POST':
        event_id = int(request.POST.get('id_evento'))
        slots = list(map(int, request.POST.getlist('slot_id[]')))
        characters = list(map(int,request.POST.getlist('character[]')))

        for index, x in enumerate(slots):
            addSlot = Slot.objects.get(id=slots[index])
            addSlot.character = Character.objects.get(id=characters[index])
            addSlot.event = Event.objects.get(id=int(event_id))
            addSlot.save()
        return redirect('/perfil')
    return render(request, 'usuarios/evento.html', context)

@login_required
def create_guild(request):
    pass
