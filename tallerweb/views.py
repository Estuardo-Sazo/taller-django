from django.shortcuts import redirect, render


def inicio(requets):
    return render(requets,'inicio/inicio.html')

def login(requets):
    return render(requets,'inicio/login.html')