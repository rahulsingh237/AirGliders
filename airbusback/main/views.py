from django.shortcuts import render

# Create your views here.
def main_app(request):

    return render(request,'main/index.html')