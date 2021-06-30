from django.shortcuts import redirect, render
import requests
from xml.etree import ElementTree as ET
from xml.dom import minidom
from requests.api import options

from requests.models import encode_multipart_formdata


endpoint='http://localhost:5000{}'

lclientes=[]
juegos=[]
mclientes=[]
juegosv=[]

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
        doc2=request.FILES['mclientes']
        doc3=request.FILES['jv']
        doc4=request.FILES['j']
        data=docs.read().decode('utf-8')
        mc=doc2.read().decode('utf-8')
        jv=doc3.read().decode('utf-8')
        j=doc4.read().decode('utf-8')
        #-----------
        linea=str(data)
        lc=linea.split('\n')
        #-----------
        linea2=str(mc)
        lmc=linea2.split('\n')
        #-----------
        linea3=str(jv)
        ljv=linea3.split('\n')
        #-----------
        linea4=str(j)
        lj=linea4.split('\n')

        for linea in lc:
            linea=linea.strip('\r')
            lc2=linea.split(',')
            lclientes.append(lc2)
        #-----------
        for linea in lmc:
            linea=linea.strip('\r')
            lmc2=linea.split(',')
            mclientes.append(lmc2)
        #-----------
        for linea in ljv:
            linea=linea.strip('\r')
            ljv2=linea.split(',')
            juegosv.append(ljv2)
        #-----------
        for linea in lj:
            linea=linea.strip('\r')
            lj2=linea.split(',')
            juegos.append(lj2)


        for linea in lclientes:
            t = document.createElement('Cliente')
            root.appendChild(t)
            nombre = document.createElement('Nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            t.appendChild(nombre)

            apellido = document.createElement('Apellido')
            apellido.appendChild(document.createTextNode(linea[1]))
            t.appendChild(apellido)

            edad = document.createElement('Edad')
            edad.appendChild(document.createTextNode(linea[2]))
            t.appendChild(edad)

            cumpleaños = document.createElement('Fecha_Cumple_Anos')
            cumpleaños.appendChild(document.createTextNode(linea[3]))
            t.appendChild(cumpleaños)

            compra = document.createElement('Primera_Compra')
            compra.appendChild(document.createTextNode(linea[4]))
            t.appendChild(compra)
        
        #----------------------
        for linea in mclientes:
            t = document.createElement('Mejores_Clientes')
            root.appendChild(t)

            nombre = document.createElement('Nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            t.appendChild(nombre)

            ucompra = document.createElement('Ultima_Compra')
            ucompra.appendChild(document.createTextNode(linea[1]))
            t.appendChild(ucompra)

            cjv = document.createElement('Juegos_Vendidos')
            cjv.appendChild(document.createTextNode(linea[2]))
            t.appendChild(cjv)

            cg = document.createElement('Cantidad_Gastada')
            cg.appendChild(document.createTextNode(linea[3]))
            t.appendChild(cg)

        #----------------------------
        for linea in jv:
            t = document.createElement('Juegos_MasVendidos')
            root.appendChild(t)

            nombre = document.createElement('Nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            t.appendChild(nombre)

            uc = document.createElement('Ultima_Compra')
            uc.appendChild(document.createTextNode(linea[1]))
            t.appendChild(uc)

            cv = document.createElement('Copias_Vendidas')
            cv.appendChild(document.createTextNode(linea[2]))
            t.appendChild(cv)

            st = document.createElement('Stoc')
            st.appendChild(document.createTextNode(linea[3]))
            t.appendChild(st)
        
        xml = root.toprettyxml(indent='\t', encoding='utf-8')

        url=endpoint.format('/datos')
        requests.post(url,xml)
        return redirect ('index')

def recibir_archivo(request):
    if request.method=='POST':
        archivo=request.FILES['document']
        adata=archivo.read()


    return redirect('index')



