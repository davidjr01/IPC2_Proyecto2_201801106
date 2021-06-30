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

        s = document.createElement('Clientes')
        root.appendChild(s)
        cont1=0
        for linea in lclientes:
            cont1=cont1+1
            t = document.createElement('Cliente_'+str(cont1))
            s.appendChild(t)

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
        s2 = document.createElement('Mejores_Clientes')
        root.appendChild(s2)
        cont2=0
        for linea in mclientes:
            cont2=cont2+1
            t = document.createElement('cliente_'+str(cont2))
            s2.appendChild(t)

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
        s3 = document.createElement('Juegos_MasVendidos')
        root.appendChild(s3)
        cont3=0
        for linea in juegosv:
            cont3=cont3+1
            t = document.createElement('Juego_'+str(cont3))
            s3.appendChild(t)

            nombre = document.createElement('Nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            t.appendChild(nombre)

            uc = document.createElement('Ultima_Compra')
            uc.appendChild(document.createTextNode(linea[1]))
            t.appendChild(uc)

            cv = document.createElement('Copias_Vendidas')
            cv.appendChild(document.createTextNode(linea[2]))
            t.appendChild(cv)

            st = document.createElement('Stock')
            st.appendChild(document.createTextNode(linea[3]))
            t.appendChild(st)

        #----------------------------
        s4 = document.createElement('Juegos')
        root.appendChild(s4)
        cont4=0
        for linea in juegos:
            cont4=cont4+1
            t = document.createElement('Juego_'+str(cont4))
            s4.appendChild(t)

            nombre = document.createElement('Nombre')
            nombre.appendChild(document.createTextNode(linea[0]))
            t.appendChild(nombre)

            p = document.createElement('Plataforma')
            p.appendChild(document.createTextNode(linea[1]))
            t.appendChild(p)

            a = document.createElement('Ano_Lanzamiento')
            a.appendChild(document.createTextNode(linea[2]))
            t.appendChild(a)

            cla = document.createElement('Clasificacion')
            cla.appendChild(document.createTextNode(linea[3]))
            t.appendChild(cla)


            
        
        xml = root.toprettyxml(indent='\t', encoding='utf-8')

        url=endpoint.format('/datos')
        requests.post(url,xml)
        return redirect ('index')

def recibir_archivo(request):
    if request.method=='POST':
        archivo=request.FILES['document']
        adata=archivo.read()


    return redirect('index')



