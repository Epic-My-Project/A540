from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('''
    <html>
    <body>
        <h1>Movie</h1>
        <ol>
            <li>image</li>
            <li>name</li>
            <li>grade</li>
            <li>rate</li>
        </ol>
        <h3>review</h3>
        very good
    </body>
    </html>
    '''
    )

def create(request):
    return HttpResponse('Create!')

def read(request, id):
    return HttpResponse('Read!' + id)