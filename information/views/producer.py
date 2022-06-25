from django.shortcuts import render

def producer(request):
    return render(request, 'producer.html')