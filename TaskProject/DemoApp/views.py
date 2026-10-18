from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class FactorialView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n = form_data.get("number")
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        # data = {
        #     "factorial" :fact
        # }
        # return JsonResponse(data)
        return JsonResponse({"factorial" :fact})


@method_decorator(csrf_exempt,name='dispatch')
class InterestView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        p = form_data.get("principal")
        t = form_data.get("time")
        r = form_data.get("rate")
        si = (p * t * r)//100
        data = {
            "principal" : p,
            "time" : t,
            "rate" : r,
            "Simple Interest" : si
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class DiscountView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        price = form_data.get("price")
        pd = form_data.get("discount_percentage")
        da = (price * pd)//100
        fp = price - da
        data = {
            "price" : price,
            "discount_percentage" : pd,
            "discount_amount" : da,
            "final_price" : fp
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        cp = form_data.get("cost_price")
        sp = form_data.get("selling_price")
        p = sp - cp
        data = {
            "cost_price" : cp,
            "selling_price" : sp,
            "Profit" : p
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        basic = form_data.get("basic")
        bonus = form_data.get("bonus")
        deduction = form_data.get("deduction")
        net = basic + bonus - deduction
        data = {
            "basic" : basic,
            "bonus" : bonus,
            "deduction" : deduction,
            "Net Salary" : net
        }
        return JsonResponse(data)