from django.shortcuts import redirect, render
import requests
from xml.etree import ElementTree as ET
from xml.dom import minidom
from requests.api import options

from requests.models import encode_multipart_formdata


endpoint='http://localhost:5000{}'

lclientes=[]

# Create your views here.
def index(request):
    if request.method=='GET':
        url=endpoint.format('/datos')
        data=requests.get(url)
        context={
            'data':data.text,
        }
        return render(request,'index.html',context)

    elif request.method=='POST':
        document = minidom.Document()
        root = document.createElement('Documento')

        docs=request.FILES['document']
        data=docs.read().decode('utf-8')
        linea=str(data)
        lc=linea.split('\n')
        for linea in lc:
            linea=linea.strip('\r')
            lc2=linea.split(',')
            lclientes.append(lc2)

        for linea in lclientes:
            tarea_e = document.createElement('Cliente')
            root.appendChild(tarea_e)
            nombre = document.createElement('nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            tarea_e.appendChild(nombre)

            apellido = document.createElement('apellido')
            apellido.appendChild(document.createTextNode(linea[1]))
            tarea_e.appendChild(apellido)

            edad = document.createElement('edad')
            edad.appendChild(document.createTextNode(linea[2]))
            tarea_e.appendChild(edad)

            cumpleaños = document.createElement('fecha_cumple_anos')
            cumpleaños.appendChild(document.createTextNode(linea[3]))
            tarea_e.appendChild(cumpleaños)

            compra = document.createElement('primera_compra')
            compra.appendChild(document.createTextNode(linea[4]))
            tarea_e.appendChild(compra)



        xml = root.toprettyxml(indent='\t', encoding='utf-8')

        url=endpoint.format('/datos')
        requests.post(url,xml)
        return redirect ('index')

def recibir_archivo(request):
    if request.method=='POST':
        archivo=request.FILES['document']
        adata=archivo.read()


    return redirect('index')



