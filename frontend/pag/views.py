from django.shortcuts import redirect, render
import requests

endpoint='http://localhost:5000{}'


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
        docs=request.FILES['document']
        data=docs.read()
        url=endpoint.format('/datos')
        requests.post(url,data)
        return redirect ('index')

