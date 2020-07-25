from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from decimal import Decimal
import time


def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


def index(request):
    num = int(request.GET.get('num'))

    time_start = datetime.now().strftime('%H:%M:%S')
    print(f'Get request at {time_start}: ', request)

    # time.sleep(5)
    result = factorial(num)
    result = str(result)[:10]

    time_end = datetime.now().strftime('%H:%M:%S')
    response_str = f'Response generated {time_start} - {time_end} \n'
    response_str += f'{num}! = {result}'

    print(response_str)
    return HttpResponse(response_str)

