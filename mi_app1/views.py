from django.shortcuts import render
from django.http import HttpResponse

def vista_1(request):
    # La vista 1 con tres etiquetas HTML diferentes: h1, p y a
    html_content = """
    <h1>Bienvenidos a mi Primera Vista</h1>
    <p>Esta es una página simple creada con Django.</p>
    <a href="vista2/">Ir a la segunda vista</a>
    """
    return HttpResponse(html_content)

def vista_2(request):
    # La vista 2 con tres etiquetas HTML diferentes: h2, p y ul
    html_content = """
    <h2>Esta es la Segunda Vista</h2>
    <p>Aquí puedes seguir explorando mi proyecto.</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
    </ul>
    """
    return HttpResponse(html_content)