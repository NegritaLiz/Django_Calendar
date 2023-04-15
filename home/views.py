from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime, timedelta


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            tarea = form.save(commit=False)
            fecha_vencimiento = form.cleaned_data['fecha_de_vencimiento']
            fecha_vencimiento_dt = datetime.combine(fecha_vencimiento, datetime.min.time()) # Convertir a datetime
            tarea.fecha_vencimiento = timezone.now() + timedelta(days=(fecha_vencimiento_dt - datetime.now()).days)
            tarea.save()

            # Enviar correo electrónico de notificación
            subject = 'Nuevo Mantenimiento Programado'
            message = 'Se ha programado el siguiente mantenimiento "{}" con fecha de vencimiento {}.'.format(tarea.Nombre_de_la_tarea, tarea.fecha_vencimiento.strftime('%d/%m/%Y'))
            from_email = 'centrodecomputos@gmail.com'
            recipient_list = ['zdelcisne1996@gmail.com',]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('home:home')

    tasks = Task.objects.all()
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def edit(request, id=id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    form = UpdateForm(request.POST or None, instance=task)
    print(form)
    return render(request, 'edit.html', {'form': form})


def completado(request, id):
        task = Task.objects.get(id=id)
        if task.completado != True:
            task.completado = True
            tarea_nombre = task.Nombre_de_la_tarea
            
            # Enviar un correo electrónico de notificación
            subject = 'Mantenimiento Completado'
            message = f'El mantenimiento de {tarea_nombre} ha sido completado.'
            from_email = 'centrodecomputos@gmail.com' # Direccion de donde se envia
            recipient_list = ['zdelcisne1996@gmail.com',] # Direccion o direcciones que recibiran el correo
            send_mail(subject, message, from_email, recipient_list)
            task.save()

            return redirect('home:home')


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home:home')


def filter_prioridad(request, choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks = Task.objects.filter(prioridad=choice)
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def filter_status(request, choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks = Task.objects.filter(completado=choice)
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})




