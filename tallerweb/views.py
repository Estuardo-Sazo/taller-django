from django.shortcuts import redirect, render


def inicio(requets):
    return render(requets,'inicio/inicio.html')