from flask import Flask,request
from flask_cors import CORS
from flask.wrappers import Response


app=Flask(__name__)
cors=CORS(app,resources={r"/*":{"origin":"*"}})


@app.route("/")
def index():
    return 'hola mundo'

@app.route('/datos',methods=['GET'])
def get_datos():
    return Response(status=200,response='asdfasdf',content_type='text/plain')

@app.route('/datos',methods=['POST'])
def post_datos():
    str_file=request.data.decode('utf-8')
    print(str_file)
    return Response(status=204)


if __name__ == "__main__":
    app.run( debug=True)