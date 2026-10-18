from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class AdditionView(View):
    def post(self,request):
        request_body = request.body
        print(request_body)
        #\r\n    "num1" : 10,\r\n    "num2" : 20\r\n

        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 + n2
        
        data = {
            "Operation" : "Addition",
            "Sum" : result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name ='dispatch')
class SubstactionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 - n2
        data = {
            "operation" : "substraction",
            "difference" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = 'dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 * n2
        data = {
            "operation" : "multiplication",
            "product" : result
        }
        return JsonResponse(data)
    

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1/n2
        data = {
            "operation" : "division",
            "division" : result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 % n2
        data = {
            "operation" : "modulus",
            "Modulus" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = 'dispatch')
class BmicalculatorView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        height = form_data.get("height")
        weight = form_data.get("weight")
        bmi = weight/((height/100)**2)
        data = {
            "height" : height,
            "weight" : weight,
            "bmi" : bmi
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = 'dispatch')
class AgeView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        birth_year = form_data.get("birth_year")
        current_year = form_data.get("current_year")
        age = current_year - birth_year
        data = {
            "Age" : age
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name = 'dispatch')
class PercentageView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        marks = form_data.get("marks")
        total_marks = form_data.get("total_marks")
        percentage = (marks/total_marks)*100
        data = {
            "Percentage" : percentage
        }
        return JsonResponse(data)