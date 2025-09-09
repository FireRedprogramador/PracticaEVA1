from django.shortcuts import render
from django.http import HttpResponse

def vista_3(request):
    # La primera vista de la App 2 con tres etiquetas HTML diferentes: h3, p y ul
    html_content = """
    <h3>Bienvenidos a la primera vista de la App 2</h3>
    <p>Esta es una lista de elementos importantes:</p>
    <ul>
        <li>Elemento A</li>
        <li>Elemento B</li>
        <li>Elemento C</li>
    </ul>
    <a href="vista4/">Ir a la segunda vista</a>
    """
    return HttpResponse(html_content)

def vista_4(request):
    # La segunda vista de la App 2 con tres etiquetas HTML diferentes: h4, p y blockquote
    html_content = """
    <h4>Esta es la segunda vista de la App 2</h4>
    <p>Aquí puedes ver una cita interesante:</p>
    <blockquote>
        "No es la especie más fuerte la que sobrevive, ni la más inteligente, sino la que mejor se adapta al cambio."
    </blockquote>
    """
    return HttpResponse(html_content)