
import json
from django.http.response import JsonResponse
from .models import products
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            product=list(products.objects.filter(id=id).values())
            if len(product)>0:
                print("si")
                produc=product[0]
                datos={'message':"success",'producto':produc}
            else:
                datos={'message':"producto no encontrado"}
            return JsonResponse(datos)  
        else:
            product= list(products.objects.values())
            if len(product)>0:
                datos={'message':"success",'productos':product}
            else:
                datos={'message':"productos no encontrados"}
            return JsonResponse(datos)   

    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        products.objects.create(pro_name=jd['pro_name'],pro_provider=jd['pro_provider'],pro_existences=jd['pro_existences'],pro_date=jd['pro_date'],pro_description=jd['pro_description'],pro_category=jd['pro_category'])

        datos={'message':"success"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd=json.loads(request.body)
        product=list(products.objects.filter(id=id).values())
        if len(product)>0:
            produc=products.objects.get(id=id)
            produc.pro_name=jd['pro_name']
            produc.pro_provider=jd['pro_provider']
            produc.pro_existences=jd['pro_existences']
            produc.pro_date=jd['pro_date']
            produc.pro_description=jd['pro_description']
            produc.pro_category=jd['pro_category']
            produc.save()
            datos={'message':"success"}
                
        else:
             datos={'message':"producto no encontrado"}

        return JsonResponse(datos)

    def delete(self,request,id):
        product=list(products.objects.filter(id=id).values())
        if len(product)>0:
            products.objects.filter(id=id).delete()
            datos={'message':"success"}
        else:
             datos={'message':"producto no encontrado"}
        return JsonResponse(datos)