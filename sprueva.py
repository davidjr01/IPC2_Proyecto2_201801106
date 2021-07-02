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
            t = document.createElement('Cliente')
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
            t = document.createElement('cliente')
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
            t = document.createElement('Juego')
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
            t = document.createElement('Juego')
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
        
        

        
#lclientes=[]
#juegos=[]
#mclientes=[]
#juegosv=[]
        for linea in lclientes:
            for i in linea[0]:
                if re.search(r'[A-Za-z ]',i):
                    xs=0
                else:
                    controlc=True
                    break

            for i in linea[1]:
                if re.search(r'[A-Za-z ]',i):
                    xs=0
                else:
                    controlc=True
                    break
            
            for i in linea[2]:
                if re.search(r'\d',i):
                    xs=0
                else:
                    controlc=True
                    break
            if re.match(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',linea[3]):
                xs=0
            else:
                controlc=True
                break
            
            if re.match(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',linea[4]):
                xs=0
            else:
                controlc=True
                break

        
        for linea in  mclientes:
            for i in linea[0]:
                if re.search(r'[A-Za-z ]',i):
                    xs=0
                else:
                    control=True
                    break

            for i in linea[2]:
                if re.search(r'\d',i):
                    xs=0
                else:
                    control=True
                    break
            

            
        
        xml = root.toprettyxml(indent='\t', encoding='utf-8')

       


