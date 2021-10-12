from django.contrib.auth.models import User
import json
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            product=list(User.objects.filter(id=id).values())
            if len(product)>0:
                print("si")
                produc=product[0]
                datos={'message':"success",'producto':produc}
            else:
                datos={'message':"producto no encontrado"}
            return JsonResponse(datos)  
        else:
            product= list(User.objects.values())
            if len(product)>0:
                datos={'message':"success",'productos':product}
            else:
                datos={'message':"productos no encontrados"}
            return JsonResponse(datos)   