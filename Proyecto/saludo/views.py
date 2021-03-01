from django.shortcuts import render

from django.http import HttpResponse
from .models import Details

# Create your views here.
def saludo(request):
   
    # type = request.POST.get('type')
    name = request.POST.get('name')
    # name = request.POST['name']

    # ejemplo de if
    try:      
        if request.method == 'POST' :
            type = request.POST['type']
            name = request.POST['name']
            obj = Details();
            obj.type = type
            obj.name = name
            obj.save();
        else:
           data = "no valid"
    except:
       print("algo paso  hpta")

   
    return render(request,'index.html',{'data':name})


def consulta(request):
   
    # type = request.POST.get('type')
    data = request.POST.get('name')    
    # ejemplo de if
    try:      
        if request.method == 'POST' :
            datos = data            
            getData = Details.objects.get(id=datos);
            # print(obj.name)
            # print(obj.type)
            data = (getData.name,getData.type)            
        else:
           data = "no valid"
    except:
       print("algo paso al traer los datos  hpta")

   
    return render(request,'consulta.html',{'data':data})