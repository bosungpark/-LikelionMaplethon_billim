from django.shortcuts import render, redirect, get_object_or_404

def notice(request):
    return render(request, 'notice.html')

def guide(request):
    return render(request, 'guide.html')

def producer(request):
    return render(request, 'producer.html')