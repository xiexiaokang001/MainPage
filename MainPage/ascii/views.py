from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .form import AsciiFrom

class AsciiViewPlus(View):
    def get(self,request):
        return render(request, 'ascii_to_char.html')
    def post(self, request):
        form = AsciiFrom(request.POST)
        if form.is_valid():
            input = str(form.cleaned_data.get('input'))
            context = input.strip().split(' ')
            result = ""
            for dst in context:
                char = chr(int(dst,16))
                if char:
                    result += str(char)
                else:
                    result += dst
            result_dict = {'result':result}
            return render(request,'ascii_to_char.html',context=result_dict)
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')


class AsciiViewMinus(View):
    def get(self,request):
        return render(request, 'char_to_ascii.html')
    def post(self, request):
        form = AsciiFrom(request.POST)
        if form.is_valid():
            input = form.cleaned_data.get('input')
            return HttpResponse(input)
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')
