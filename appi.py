from flask import Flask,request
from flask_cors import CORS
from flask.wrappers import Response


app=Flask(__name__)
cors=CORS(app,resources={r"/*":{"origin":"*"}})


@app.route("/")
def index():
    return 'hola muxzcvzxcvndo'

@app.route('/datos',methods=['GET'])  ##es el que manda datos
def get_datos():
    abrir=open('guardar.txt','r+')
    return Response(status=200,response=abrir.read(),content_type='text/plain')

@app.route('/datos',methods=['POST'])   ## es el que recibe datos
def post_datos():
    str_file=request.data.decode('utf-8')
    guardar=open('guardar.txt','w+')
    guardar.write(str_file)
    guardar.close()
    print(str_file)
    return Response(status=204)


if __name__ == "__main__":
    app.run( debug=True)