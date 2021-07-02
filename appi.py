from flask import Flask,request
from flask_cors import CORS
from flask.wrappers import Response
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as xml


app=Flask(__name__)
cors=CORS(app,resources={r"/*":{"origin":"*"}})


@app.route("/")
def index():
    return 'hola muxzcvzxcvndo'

@app.route('/datos',methods=['GET'])  # manda datos
def get_datos():
    abrir=open('guardar2.xml','r+')
    return Response(status=200,response=abrir.read(),content_type='text/plain')

@app.route('/graficas',methods=['GET'])  # manda datos
def get_graficas():
    a=[]
    tree = ET.parse('guardar2.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)

    return Response(status=200,response="asss",content_type='text/plain')


@app.route('/datos',methods=['POST'])   ##recibe datos
def post_datos():
    str_file=request.data
    guardar=open('guardar2.xml','wb')
    guardar.write(str_file)
    guardar.close()
    
    return Response(status=204)


if __name__ == "__main__":
    app.run( debug=True)