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
            input_str = form.cleaned_data.get('input')
            result = ""
            for char in input_str:
                result += hex(ord(char))[2:] + " "
            return render(request, 'char_to_ascii.html', {'result': result.strip()})
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')

class AsciiViewReverse(View):
    def get(self,request):
        return render(request, 'string_reverse.html')
    def post(self, request):
        form = AsciiFrom(request.POST)
        if form.is_valid():
            input_str = form.cleaned_data.get('input')
            result = input_str[::-1]
            return render(request, 'string_reverse.html', {'result': result})
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')
