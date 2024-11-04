from django.shortcuts import render, redirect
from .models import Ruta, Horario, Bus, Boleto
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "ventas/home.html")

def profile_view(request):
    return render(request,'accounts/profile.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Tu cuenta ha sido creada exitosamente. Puedes iniciar sesión."
            )
            return redirect("login")  # Redirigir a la página de inicio de sesión
    else:
        form = UserCreationForm()

    return render(request, "ventas/register.html", {"form": form})


@login_required
def lista_horarios(request):
    horarios = Horario.objects.all()
    return render(request, "ventas/lista_horarios.html", {"horarios": horarios})


@login_required
def vender_boleto(request, bus_id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        documento = request.POST["documento"]
        bus = Bus.objects.get(id=bus_id)
        if bus.boleto_set.count() < bus.capacidad:
            Boleto.objects.create(
                bus=bus,
                nombre_pasajero=nombre,
                documento_identidad=documento,
                usuario=request.user,
            )
            return HttpResponse("Boleto vendido exitosamente")
        else:
            return HttpResponse("No quedan asientos disponibles")
    else:
        return render(request, "ventas/vender_boleto.html", {"bus_id": bus_id})


@login_required
def mis_boletos(request):
    boletos = Boleto.objects.filter(usuario=request.user)
    return render(request, "ventas/mis_boletos.html", {"boletos": boletos})
